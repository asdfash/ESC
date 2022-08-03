import unittest
import pandas as pd
from functions import export
import os



import random

def fuzz(f,iter,minrange = 2, maxrange = 64):
    for i in range(iter):
        r = random.randbytes(random.randrange(minrange,maxrange))
        


class exportExcelTestCases(unittest.TestCase):
    def test_export_file_successfully(self):
        try:
            os.remove("C:/Users/JN/Desktop/Cologne/ESC/unittest/in-excel-not-gdb.xlsx")
        except:
            pass
        try:
            os.remove("C:/Users/JN/Desktop/Cologne/ESC/unittest/in-gdb-not-excel.xlsx")
        except:
            pass    
        df1= pd.DataFrame([[1, 2, 3], [4, 5, 6]])
        df2= pd.DataFrame([[7, 8, 9],[10, 11, 12]])
        export(df1,df2,"C:/Users/JN/Desktop/Cologne/ESC/")
        self.assertTrue(os.path.exists("C:/Users/JN/Desktop/Cologne/ESC/unittest/in-excel-not-gdb.xlsx"))
        self.assertTrue(os.path.exists("C:/Users/JN/Desktop/Cologne/ESC/unittest/in-gdb-not-excel.xlsx"))

    def test_export_file_successfully_fuzzed(self):
        
        iter = 1000
        minrange = 2
        maxrange = 1000

        for i in range(iter):
            try:
                os.remove("C:/Users/JN/Desktop/Cologne/ESC/in-excel-not-gdb.xlsx")
            except:
                pass
            try:
                os.remove("C:/Users/JN/Desktop/Cologne/ESC/in-gdb-not-excel.xlsx")
            except:
                pass    
            r1 = random.randbytes(random.randrange(minrange,maxrange))
            r2 = random.randbytes(random.randrange(minrange,maxrange))
            df1= pd.DataFrame(list(r1))
            df2= pd.DataFrame(list(r2))
            export(df1,df2,"C:/Users/JN/Desktop/Cologne/ESC/")
            self.assertTrue(os.path.exists("C:/Users/JN/Desktop/Cologne/ESC/in-excel-not-gdb.xlsx"))
            self.assertTrue(os.path.exists("C:/Users/JN/Desktop/Cologne/ESC/in-gdb-not-excel.xlsx"))


if __name__ == '__main__':
        unittest.main()