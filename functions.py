import pandas as pd
import os
import datetime
import arcpy


def logfile(logpath,timestamp):
    try:
        lf = open(logpath + timestamp + '.log', 'w')
        log = True
        print("log file created")
    except:
        print("log file failed to be created, conintuing")
        log = False
        lf =""
    return lf,log

def logprint(msg,lf="",log=0,close =False):
    print(msg)
    if log:
        lf.write(msg + "\n")
        if close:
            lf.close()

def excelfile(excelpath,lf="",log=0):
    try:
        logprint("importing excel file",lf,log)

        if excelpath == "":
            error = "error reading excel file or no file selected\n"
            logprint(error,lf,log,close=True)
            return -1
            
        column_list = []
        data_column = pd.read_excel(excelpath).columns
        for i in data_column:
            column_list.append(i)
        converter = {col: str for col in column_list} 
        data = pd.read_excel(excelpath, converters=converter) #read the dataframe as str datatype
        logprint("excel file imported",lf,log)
        return data
    except:
        error = "error reading excel file or no file selected\n"
        logprint(error,lf,log,close=True)
        return -1

def gdbdata(gdbpath,lf="",log=0):
    try:
        #get gdb
        logprint("importing gdb data",lf,log)
        featureclasslist = arcpy.ListFeatureClasses("*")
        gdb=[]
        desc = arcpy.Describe(gdbpath+featureclasslist[0])
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
        logprint("gdb data imported",lf,log)
        return df
    except:
        error = "error reading gdb file or no file selected\n"
        logprint(error,lf,log,close=True)
        return -1

def compare(df,data,lf="",log=0):
    try:
        logprint("copmaring data",lf,log)    
        data_cols = data.columns
        df_compare = df.loc[:,data_cols] # remove columns that are not in exelsheet
        dataout1 = dataframe_difference(df_compare, data, which="right_only").drop(["_merge"], axis=1) #find difference
        dataout2 = dataframe_difference(df_compare, data, which="left_only").drop(["_merge"], axis=1) #find difference
        logprint("data compared",lf,log)
        return dataout1,dataout2
    except:
        error = "error comparing, check header names or custom header\n"
        logprint(error,lf,log,close=True)
        return -1, -1

def export(dataout1,dataout2,outputpath,lf="",log=0):
    try:
        logprint("exporting excel file",lf,log)
        dataout1.to_excel(outputpath + "in-exel-not-gdb.xlsx",index = False)
        dataout2.to_excel(outputpath + "in-gdb-not-exel.xlsx",index = False)
        logprint("excel file exported",lf,log)
    except:
        error = "error reading destination or no folder was selected selected\n"
        logprint(error,lf,log,close=True)

#https://hackersandslackers.com/compare-rows-pandas-dataframes/
def dataframe_difference(df1, df2, which=None):
    df1 = df1.astype('string',errors='ignore')
    df2 = df2.astype('string',errors='ignore')
    df1 = df1.astype('int64',errors='ignore')
    df2 = df2.astype('int64',errors='ignore')
    comparison_df = df1.merge(
        df2,
        indicator=True,
        how='outer',
        sort = True
    )
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    return diff_df


def main(excelpath,gdbpath,outputpath,logpath,keyword, header,customtext):
    arcpy.env.workspace = gdbpath
    #variables
    timestamp = str(datetime.datetime.now()).replace(" ","").replace(".","").replace(":","")

    #clean up inputs
    if excelpath[-2:] == "\n":
        excelpath = excelpath[:-2]
    if outputpath[-2:] == "\n":
        outputpath = outputpath[:-2]
    if gdbpath[-2:] == "\n":
        gdbpath = gdbpath[:-2]
    if logpath[-2:] == "\n":
        logpath = logpath[:-2]
    if keyword[-2:]== "\n":
        keyword = keyword[:-2]
    if header[-2:]== "\n":
        header = header[:-2]
    if customtext[-2:]== "\n":
        customtext = customtext[:-2]


    #make log folder amd file
    try:
        if not os.path.exists(logpath):
            print("log folder not found, creating one")
            os.mkdir(logpath)
        lf,log = logfile(logpath,timestamp)
    except:
        print("error creating log folder, continuing")
        lf =""
        log = False

    #import excel file
    data = excelfile(excelpath,lf,log)
    if data == -1:
        return

    #import gdb data
    df = gdbdata(gdbpath,lf,log)
    if df == -1:
        return
    
    #process optional features
    logprint("processing with optional features",lf,log)
    try:
        keyword = "".join(keyword.split())
        header = "".join(header.split())
        if keyword.split() != "" and header != "":
            df = df[df[header]== keyword] # remove rows that do not fit this condition
        customtext = customtext.split()
        if len(customtext) == data.shape[0]:
            data.columns = customtext
        elif customtext != []:
            logprint("custom header text found, but not correct number, double check spacing",lf,log)
           
        logprint("optional features processed",lf,log)
    except:
        error = "error with processing optional features, taking it as null and continuing\n"
        logprint(error,lf,log)

    #compare
    dataout1 , dataout2 = compare(df,data, lf,log)
    if dataout1 == -1:
        return

    #export file
    export(dataout1,dataout2,outputpath,lf,log)