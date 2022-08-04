
import unittest
from functions import *

print(logfile)

class logTestCases(unittest.TestCase):
    def test_logfile(self):
        logTest = logfile
        self.assertTrue(logTest)       
        
    def test_logprint(self):
        msgTest = logprint
        self.assertNotEqual("",msgTest)
        
        
if __name__ == '__main__':
    unittest.main()