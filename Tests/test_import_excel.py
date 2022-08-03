import unittest
from import_excel import *

class excelFileTestCases(unittest.TestCase):
    def test_df_foramt(self):
        dataframe = import_excel(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel1.xlsx")
        self.assertTrue(isinstance(dataframe, pd.DataFrame))
    
    def test_blank_data(self):
        dataframe = import_excel(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\TestGDBExcel1.xlsx")
        for col in dataframe.columns:
            self.assertTrue(dataframe[col].isna().sum()<1)

if __name__ == '__main__':
        unittest.main()
    

             