
import random 
import copy
from  functions import *


excelpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\Unit Attributes(PIDB).xlsx"
gdbpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TPY_Batch12.gdb"
recordpath = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Tests"

def fuzzing (exceldata, gdbdata):
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

def randomFuzzing(exceldata, gdbdata):
    i=0
    col = exceldata.columns
    num_data = exceldata.shape[0]
    data = copy.deepcopy(exceldata)
    while(True):
        randint1 = random.randint(0, num_data-1)
        randint2 = random.randint(0, len(col)-1)
        randnum = random.randint(10000,100000)
        data.at[randint1, col[randint2]] = randnum
        dataout1, dataout2 = compare(gdbdata, data)
        i+=1
        print(dataout2.shape[0], i)
        if(dataout2.shape[0] == gdbdata.shape[0]):
            break

def columnFuzzing(exceldata, gdbdata):
    data = copy.deepcopy(exceldata)
    num_col = exceldata.shape[1]
    i = 0
    while(True):
        print(data)
        col_list = list(data)
        randint1 = random.randint(0, num_col-1)
        randint2 = random.randint(0, num_col-1)
        col_list[randint1], col_list[randint2] = col_list[randint2], col_list[randint1]
        data.columns = col_list
        dataout1, dataout2 = compare(gdbdata, data)
        i+=1
        print(dataout2.shape[0], i)

def rowFuzzing(exceldata, gdbdata):
    data = copy.deepcopy(exceldata)
    num_data = exceldata.shape[0]
    i = 0
    while(True):
        print(data)
        col_list = list(data)
        randint1 = random.randint(0, num_data-1)
        randint2 = random.randint(0, num_data-1)
        row1, row2 = data.iloc[randint1], data.iloc[randint2]
        data.iloc[0], data.iloc[1] = row2, row1
        dataout1, dataout2 = compare(gdbdata, data)
        i+=1
        print(dataout2.shape[0], i)
    
arcpy.env.workspace = gdbpath            
exceldata = excelfile(excelpath)
gdb = gdbdata(gdbpath)
gdb = gdb[gdb["NUM_TYPE"]== "STRATA"]
# fuzzing(exceldata, gdb)
# randomFuzzing(exceldata, gdb)
# columnFuzzing(exceldata, gdb)
rowFuzzing(exceldata, gdb)



