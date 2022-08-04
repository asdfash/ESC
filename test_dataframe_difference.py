import unittest
import pandas as pd
from functions import dataframe_difference

class dataframeDifferenceTestCases(unittest.TestCase):
    def test_same_dataframe(self):
        df = pd.DataFrame([[1, 2, 3],[4, 5, 6]])
        difference = dataframe_difference(df, df)
        self.assertTrue(len(difference)==0)
    
    def test_same_data_diff_order(self):
        df1 = pd.DataFrame([[1, 2, 3],[4, 5, 6]])
        df2 = pd.DataFrame([[4, 5, 6], [1, 2, 3]])
        difference = dataframe_difference(df1, df2)
        self.assertTrue(len(difference)==0)

    def test_different_dataframe_size(self):
        df1 = pd.DataFrame([[1, 2, 3],[4, 5, 6]])
        df2 = pd.DataFrame([[4, 5, 6]])
        difference = dataframe_difference(df1, df2)
        self.assertTrue(len(difference)==1)


    


if __name__ == '__main__':
        unittest.main()