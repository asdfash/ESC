import unittest
from import_excel import *

class excelFileTestCases(unittest.TestCase):
    def test_df_foramt(self):
        dataframe = import_excel(r"D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\Unit Attributes(PIDB).xlsx")
        self.assertTrue(isinstance(dataframe, pd.DataFrame))

if __name__ == '__main__':
        unittest.main()
    

             