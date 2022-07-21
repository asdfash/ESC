import pandas as pd
import os
import datetime
import arcpy



def main(excelpath,gdbpath,outputpath,logpath,keyword="STRATA", header="NUM_TYPE"):
    arcpy.env.workspace = gdbpath

    #variables
    timestamp = str(datetime.datetime.now()).replace(" ","").replace(".","").replace(":","")

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
        exit()

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
    print(df)


    #TODO: check files

    data_cols = data.columns
    # df = df[col_name]
    # dataout = pd.DataFrame()
    # for i in col_name:
    #     dataout[f'Check_{i}'] = np.where(data[i] == df[i], True, False)
    # dataout['Overall_check'] = dataout.all(axis='columns')
    # if log:
    #     lf.write("data comparison finished\n")
    df = df[df[header]== keyword] # remove rows that do not fit this condition
    df_compare = df.loc[:,data_cols] # remove columns that are not in exelsheet
    ##########

    #TODO: 1. test this with fixed excel file and see if work
    #TODO: 3. if empty dont make excel file (optional aka not tonight)

    dataout1 = dataframe_difference(df_compare, data, which="right_only").drop(["_merge"], axis=1) #find difference
    dataout2 = dataframe_difference(df_compare, data, which="left_only").drop(["_merge"], axis=1) #find difference

    #export file
    if outputpath == "":
        error = "error reading destination or no folder was selected selected\n"
        print(error)
        if log:
            lf.write(error)
            lf.close()
        return

    #TODO: 2. rename output names to something more sensible eg. in_excel_but_wrong_or_not_in_gdb_, ect (i not good with names)
    dataout1.to_excel(outputpath + "export1.xlsx",index = False)
    dataout2.to_excel(outputpath + "export2.xlsx",index = False)
    print("excel file exported\n")
    if log:
        lf.write("excel file exported\n")
        # cleanup
        lf.close()



#https://hackersandslackers.com/compare-rows-pandas-dataframes/
def dataframe_difference(df1, df2, which=None):
    df1 = df1.astype('string',errors='ignore')
    df2 = df2.astype('string',errors='ignore')
    df1 = df1.astype('int64',errors='ignore')
    df2 = df2.astype('int64',errors='ignore')
    print(df1.dtypes)
    print(df2.dtypes)
    comparison_df = df1.merge(
        df2,
        indicator=True,
        how='outer',
        sort = True
    )
    print(comparison_df)
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    return diff_df


    #TODO: 4. try except different parts and add print/log statements for error checking (optional)
    #TODO: 5. refactor code to be able to test different things (optional)