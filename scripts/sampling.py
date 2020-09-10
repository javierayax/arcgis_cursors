# Sampling
# imports
import arcpy  # ArcGIS Desktop / ArcGIS Server
import random

# Variables
coca_fc = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\coca"

# Parameters
size = arcpy.GetParameter(0)

# Identify ids
oids_list = []
cursor = arcpy.da.SearchCursor(coca_fc, "OBJECTID")
for row in cursor:
    oid = row[0]
    oids_list.append(oid)

# Select random oids
sample = random.sample(oids_list, size)

# Build where condition
where = "OBJECTID IN ("
for oid in sample:
    where += str(oid) + ","

where = where[:-1] + ")"
arcpy.AddMessage(where)

# Create layer
out_layer = arcpy.management.MakeFeatureLayer("Coca", "Coca_Samples", where)

# Add to map
arcpy.SetParameter(1, out_layer)

# End
