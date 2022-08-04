import unittest
import pandas as pd
from functions import compare
from os import execle
import numpy as np

class CompareTestCases(unittest.TestCase):
    def test_error_comparison(self):
        inputexcel = r"D:\Haozhi\SUTD\50.003\TestGDBExcel(F).xlsx"#has wrong header
        inputgdb = r"D:\Haozhi\SUTD\50.003\testGDB.gdb"
        result = compare(inputgdb,inputexcel)
        self.assertTrue(result[0] == -1, result[1] == -1)





if __name__ == '__main__':
        unittest.main()