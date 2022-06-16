import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
import datetime
import arcpy
import numpy as np


#settings
filename = os.path.basename("__file__")
workingdir = "__file__"[:len("__file__")-len(filename)]
logdir = workingdir + 'logs'
arcpy.env.workspace = workingdir + "testGDB.gdb"

#variables
timestamp = str(datetime.datetime.now()).replace(" ","").replace(".","").replace(":","")

#startup
root=tk.Tk()
root.withdraw()

#make log folder
if not os.path.exists(logdir):
    os.mkdir(logdir)

#make log file
try:
    lf = open(workingdir + 'logs/' + timestamp + '.log', 'w')
    log = True
except:
    print("log file failed to be created, conintuing")
    log = False

#import excel file
f = filedialog.askopenfilename(initialdir=workingdir, filetypes=[("Excel files", "*.xlsx")])
if f == "":
    error = "error reading excel file or no file selected, exiting\n"
    print(error)
    if log:
        lf.write(error)
    lf.close()
    exit()
column_list = []
data_column = pd.read_excel(f, 'Sheet1').columns
for i in data_column:
    column_list.append(i)
converter = {col: str for col in column_list} 
data = pd.read_excel(f, converters=converter) #read the dataframe as str datatype
print("excel file imported")
if log:
    lf.write("excel file imported\n")

print(data)

#get gdb
featureclasslist = arcpy.ListFeatureClasses("*")
gdb=[]
desc = arcpy.Describe(workingdir + "testGDB.gdb/"+featureclasslist[0])
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
dest = filedialog.askdirectory(initialdir=workingdir)
if dest == "":
    error = "error reading destination or no folder was selected selected, exiting\n"
    print(error)
    if log:
        lf.write(error)
    lf.close()
    exit()

dataout.to_excel(dest + "/export.xlsx",index = False)
if log:
    lf.write("excel file exported\n")



# cleanup
lf.close()
root.destroy()