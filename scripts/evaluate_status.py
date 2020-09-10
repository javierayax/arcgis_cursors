# Evaluate status
# imports
import arcpy

# Variables
samples = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\muestreorevisado"
grids = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\grillacoca"

with arcpy.da.UpdateCursor(grids, ["indice10k", "estado"], "estado = 'En control'") as updateCursor:
    for grid in updateCursor:
        index = grid[0]
        where = "indice10k = '" + index + "'"
        grid_status = "Validada"
        with arcpy.da.SearchCursor(samples, ["indice10k", "estado"], where) as searchCursor:
            for sample in searchCursor:
                sample_status = sample[1]
                if sample_status == "Rechazado":
                    grid_status = "Por verificar"
                    break
        grid[1] = grid_status
        updateCursor.updateRow(grid)

# end
