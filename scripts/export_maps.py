# Export maps
# Imports
import arcpy

# Variables
grids = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\grillacoca"
aprx_path = r"C:\jescudero\Esri\Webinar_cursores\ControlCalidad.aprx"
out_folder = r"C:\jescudero\Esri\Webinar_cursores\maps"

# Identify layout
aprx = arcpy.mp.ArcGISProject(aprx_path)
layout = aprx.listLayouts()[0]
mapframe = layout.listElements("MAPFRAME_ELEMENT")[0]
title = layout.listElements("TEXT_ELEMENT", "title")[0]

# Iterate through rows
with arcpy.da.SearchCursor(grids, ["SHAPE@", "Indice10k", "estado"]) as cursor:
    for row in cursor:
        shape = row[0]
        index = row[1]
        status = row[2]

        if status == "Validada":
            extent = shape.extent
            # change extent
            mapframe.camera.setExtent(extent)
            # change scale
            mapframe.camera.scale = int(mapframe.camera.scale*1.3)
            # change title
            title.text = "Grilla: " + index
            # export
            layout.exportToPNG(out_folder + "\\mapa_" + index + ".png")

# End
