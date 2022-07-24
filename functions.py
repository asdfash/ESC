import pandas as pd
import os
import datetime
import arcpy



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
    #make log folder
    if not os.path.exists(logpath):
        os.mkdir(logpath)

    #make log file
    try:
        lf = open(logpath + timestamp + '.log', 'w')
        log = True
        print("log file created")
    except:
        print("log file failed to be created, conintuing")
        log = False

    #import excel file
    try:
        if excelpath == "":
            error = "error reading excel file or no file selected\n"
            print(error)
            if log:
                lf.write(error)
                lf.close()
            return
            
        column_list = []
        data_column = pd.read_excel(excelpath).columns
        for i in data_column:
            column_list.append(i)
        converter = {col: str for col in column_list} 
        data = pd.read_excel(excelpath, converters=converter) #read the dataframe as str datatype
        print("excel file imported")
        if log:
            lf.write("excel file imported\n")
    except:
        error = "error reading excel file or no file selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return
    try:
        #get gdb
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
        
        print("gdb data imported")
        if log:
            lf.write("gdb data imported\n")

    except:
        error = "error reading gdb file or no file selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return

    
    
        #preprocessing optional features
    print("preprocessing optional features")
    if log:
        lf.write("preprocessing optional features\n")
    try:
        keyword = "".join(keyword.split())
        header = "".join(header.split())
        if keyword.split() != "" and header != "":
            df = df[df[header]== keyword] # remove rows that do not fit this condition
        customtext = customtext.split()
        if len(customtext) == data.shape[0]:
            data.columns = customtext
        elif customtext != []:
            print("custom header text found, but not correct number, double check spacing ")
            if log:
                lf.write("custom header text found, but not correct number, double check spacing\n")
           
        print("optional features processed")
        if log:
            lf.write("optional features processed\n")
    except:
        error = "error with processing optional features, taking it as null and continuing\n"
        print(error)
        if log:
            lf.write(error)
    ##########

    #TODO: 3. if empty dont make excel file (optional aka not tonight)
    try:
        data_cols = data.columns
        df_compare = df.loc[:,data_cols] # remove columns that are not in exelsheet
        dataout1 = dataframe_difference(df_compare, data, which="right_only").drop(["_merge"], axis=1) #find difference
        dataout2 = dataframe_difference(df_compare, data, which="left_only").drop(["_merge"], axis=1) #find difference
    except:
        error = "error comparing, check header names or custom header\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return
    #export file
    try:
        print("exporting excel file")
        dataout1.to_excel(outputpath + "in-exel-not-gdb.xlsx",index = False)
        dataout2.to_excel(outputpath + "in-gdb-not-exel.xlsx",index = False)
        print("excel file exported\n")
        if log:
            lf.write("excel file exported\n")
            lf.close()
            return
    except:
        error = "error reading destination or no folder was selected selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return



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


    #TODO: 4. try except different parts and add print/log statements for error checking (optional)
    #TODO: 5. refactor code to be able to test different things (optional)