from genericpath import exists
from time import sleep
import unittest
import pandas as pd
from functions import export
import os

class exportExcelTestCases(unittest.TestCase):
    def test_export_file_successfully(self):
        df1= pd.DataFrame([[1, 2, 3], [4, 5, 6]])
        df2= pd.DataFrame([[7, 8, 9],[10, 11, 12]])
        export(df1,df2,"C:/Users/JN/Desktop/Cologne/ESC/")
        self.assertTrue(os.path.exists("in-excel-not-gdb.xlsx"))

    


if __name__ == '__main__':
        unittest.main()