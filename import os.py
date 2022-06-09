

# import tkinter as tk
# from tkinter import filedialog
# import pandas as pd
# import os
# import datetime


# #settings
# filename = os.path.basename(__file__)
# workingdir = __file__[:len(__file__)-len(filename)]
# logdir = workingdir + 'logs'

# #variables
# timestamp = str(datetime.datetime.now()).replace(" ","").replace(".","").replace(":","")

# #startup
# root=tk.Tk()
# root.withdraw()

# #make log folder
# if not os.path.exists(logdir):
#     os.mkdir(logdir)

# #make log file
# try:
#     lf = open(workingdir + 'logs/' + timestamp + '.log', 'w')
#     log = True
# except:
#     print("log file failed to be created, conintuing")
#     log = False

# #import excel file
# f = filedialog.askopenfilename(initialdir=workingdir, filetypes=[("Excel files", "*.xlsx")])
# if f == "":
#     error = "error reading excel file or no file selected, exiting\n"
#     print(error)
#     if log:
#         lf.write(error)
#     lf.close()
#     exit()
# data = pd.read_excel(f)
# if log:
#     lf.write("excel file imported\n")

# #export file
# dest = filedialog.askdirectory(initialdir=workingdir)
# if dest == "":
#     error = "error reading destination or no folder was selected selected, exiting\n"
#     print(error)
#     if log:
#         lf.write(error)
#     lf.close()
#     exit()
# data.to_excel(dest + "/export.xlsx",index = False)
# if log:
#     lf.write("excel file exported\n")



# # cleanup
# lf.close()
# root.destroy()

import arcpy
from arcpy import env,da
env.workspace = r"C:\Users\jitth\Desktop\ESC\testGDB.gdb"
i = 1
for fc in arcpy.ListFeatureClasses("*"):
        count = da.TableToNumPyArray(fc,"*")
        print (count)

        # df = pd. DataFrame()
        # filepath = r"C:\Users\jitth\Desktop\ESC\table" + str(i)
        # df.to_excel(filepath,index=False)
        # i += 1
