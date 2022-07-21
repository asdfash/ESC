import unittest
import pandas as pd
import os

#check file type in correct or incorrect format
class TestExcel(unittest.TestCase):
    def runTest(self):
        data = "comparefile1.xlsx"
        word = os.path.splitext(data)
        file_name = word[0]
        file_extension = word[1]
    
        if data.endswith(".xlsx"):
            print("Correct file type")
            print("File Name:", file_name)
            print("File Extension:", file_extension)
        else:
            print("Incorrect file type given:{} , please provide excel file instead".format(word[1]))


#run the test
if __name__ == '__main__':
    unittest.main()
        
        
        
        

   