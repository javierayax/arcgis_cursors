# insert samples
# imports
import arcpy
import random

# Variables
coca_fc = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\coca"
coca_sample = r"C:\jescudero\Esri\Webinar_cursores\data\data.gdb\muestreo"

insertor = arcpy.da.InsertCursor(coca_sample, ["Estado"])
# insertor.insertRow(("Por revisar"))
del insertor

insertor = arcpy.da.InsertCursor(coca_sample, ["Estado", "SHAPE@"])

# Identify ids
oids = [row[0] for row in arcpy.da.SearchCursor(coca_fc, ["OBJECTID"])]

# Select random oids
sample = random.sample(oids, 500)
with arcpy.da.SearchCursor(coca_fc, ["OBJECTID", "SHAPE@"]) as cursor:
    for row in cursor:
        oid, shape = row
        if oid in sample:
            insertor.insertRow(("Por revisar", shape))

del insertor

# End
