from argparse import FileType
from platform import system
import pandas as pd
import numpy as np


#compare differences of 2 excel files
df1 = pd.read_excel('comparefile1.xlsx')

df2 = pd.read_excel("comparefile2.xlsx")    
df1.equals(df2)

comparison_values = df1.values == df2.values
print(df1)
print(df2)
print(comparison_values)

#export differences to new excel file
rows, cols = np.where(comparison_values == False)
for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])

df1.to_excel('./Excel_diff.xlsx', index = False, header = True)

#check excel file exist
#fName = "nonexcel.txt"
fName = "Excel_diff.xlsx"
try:
    if fName.endswith(".xlsx"):
        f = open(fName, 'rb')
        print("successfully created new excel file of differences")
    else:
        print("not excel file")
except FileNotFoundError:
    print("cant find file, please redo")
    
