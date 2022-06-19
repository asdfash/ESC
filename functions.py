import pandas as pd
import os
import datetime
import arcpy
import numpy as np



def main(excelpath,gdbpath,outputpath,logpath):
    arcpy.env.workspace = gdbpath

    #variables
    timestamp = str(datetime.datetime.now()).replace(" ","").replace(".","").replace(":","")

    #make log folder
    if not os.path.exists(logpath):
        os.mkdir(logpath)

    #make log file
    try:
        print(logpath)
        lf = open(logpath + timestamp + '.log', 'w')
        log = True
    except:
        print("log file failed to be created, conintuing")
        log = False

    #import excel file

    if excelpath == "":
        error = "error reading excel file or no file selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return
    column_list = []
    data_column = pd.read_excel(excelpath, 'Sheet1').columns
    for i in data_column:
        column_list.append(i)
    converter = {col: str for col in column_list} 
    data = pd.read_excel(excelpath, converters=converter) #read the dataframe as str datatype
    print("excel file imported")
    if log:
        lf.write("excel file imported\n")

    print(data)

    #get gdb
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
    print(df)

    #TODO: check files
    col_name = data.columns
    df = df[col_name]
    dataout = pd.DataFrame()
    for i in col_name:
        dataout[f'Check_{i}'] = np.where(data[i] == df[i], True, False)
    dataout['Overall_check'] = dataout.all(axis='columns')
    print(dataout)


    #export file
    if outputpath == "":
        error = "error reading destination or no folder was selected selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return

    dataout.to_excel(outputpath + "export.xlsx",index = False)
    if log:
        lf.write("excel file exported\n")
        # cleanup
        lf.close()