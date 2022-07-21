import unittest
from import_gdb import *

class excelFileTestCases(unittest.TestCase):
    def test_df_foramt(self):
        dataframe = import_gdb(r'D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\testGDB.gdb')
        self.assertTrue(isinstance(dataframe, pd.DataFrame))
   
if __name__ == '__main__':
        unittest.main()
    