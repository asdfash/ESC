from os import execle
import unittest
from functions import *

class excelFileTestCases(unittest.TestCase):
    def test_format(self):
        input = r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel.xlsx"
        self.assertTrue(input.endswith(".xlsx"))

    def test_empty_excel(self):
        dataframe= excelfile(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel.xlsx")
        self.assertFalse(dataframe.empty)

    def test_df_foramt(self):
        dataframe = excelfile(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel.xlsx")
        self.assertTrue(isinstance(dataframe, pd.DataFrame))
    
    def test_blank_entry(self):
        dataframe = excelfile(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel.xlsx")
        for col in dataframe.columns:
            self.assertTrue(dataframe[col].isna().sum()<1)

if __name__ == '__main__':
    unittest.main()
    

             