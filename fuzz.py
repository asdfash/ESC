
import random 
import copy
from  functions import *
from import_gdb import *


excelpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\Unit Attributes(PIDB).xlsx"
gdbpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TPY_Batch12.gdb"
recordpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Tests"

def fuzz (exceldata, gdbdata):
    lf = open(recordpath + r"\fuzzerRecords.txt", 'w') 
    lf.write("No of data: " + str(gdbdata.shape[0]) + "\n")
    for j in exceldata.columns:
        data = copy.deepcopy(exceldata)
        lf.write("Changing " + j + "\n")
        for i in range(data.shape[0]):
            data.at[i, j ] = random.randint(10000,100000)
            dataout1, dataout2 = compare(gdbdata, data)
            diff = (dataout2.shape[0], i)
            lf.write(str(diff) + "\n")
            print(dataout2.shape[0], i)
        lf.write("\n\n\n\n\n\n\n\n\n")
    lf.close()

arcpy.env.workspace = gdbpath            
exceldata = excelfile(excelpath)
gdb = gdbdata(gdbpath)
gdb = gdb[gdb["NUM_TYPE"]== "STRATA"]
fuzz(exceldata, gdb)





