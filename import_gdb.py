import arcpy
import pandas as pd

def import_gdb(gdbpath):
    arcpy.env.workspace = gdbpath
    featureclasslist = arcpy.ListFeatureClasses("*")
    gdb=[]
    desc = arcpy.Describe(gdbpath+'/'+featureclasslist[0])
    label=[]
    for field in desc.fields:
        label += [field.name]
    for fc in featureclasslist:
        for datar in arcpy.da.TableToNumPyArray(fc,"*"):
            row = []
            for i in datar:
                row +=[i]
            gdb+=[row]
    df = pd.DataFrame(gdb, columns= label)
    return df

