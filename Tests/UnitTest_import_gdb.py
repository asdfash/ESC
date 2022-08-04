import unittest
from functions import *
import numpy as np

class gdbFileTestCases(unittest.TestCase):
    def test_format(self):
        input = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB.gdb"
        self.assertTrue(input.endswith(".gdb"))

    def test_empty_gdb(self):
        dataframe= gdbdata(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB.gdb")
        self.assertFalse(dataframe.empty)

    def test_df_foramt(self):
        dataframe = gdbdata(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB.gdb")
        self.assertTrue(isinstance(dataframe, pd.DataFrame))
    
    def test_blank_entry(self):
        dataframe = gdbdata(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB.gdb")
        dataframe = dataframe.replace('', np.nan) 
        for col in dataframe.columns:  
            self.assertTrue(dataframe[col].isna().sum()<1)
   
if __name__ == '__main__':
    arcpy.env.workspace = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB.gdb"
    unittest.main()
    