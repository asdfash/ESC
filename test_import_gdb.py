import unittest
from import_gdb import *
import numpy as np

class excelFileTestCases(unittest.TestCase):
    def test_df_foramt(self):
        dataframe = import_gdb(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB1.gdb")
        self.assertTrue(isinstance(dataframe, pd.DataFrame))
    
    def test_blank_data(self):
        dataframe = import_gdb(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB1.gdb")
        dataframe = dataframe.replace('', np.nan) 
        for col in dataframe.columns:  
            self.assertTrue(dataframe[col].isna().sum()<1)
   
if __name__ == '__main__':
        unittest.main()
    