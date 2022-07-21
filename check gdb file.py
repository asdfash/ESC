#test for null/blank gdb file

import os

file_path =  "D:\SUTD\Term_5\50.003_Elements of Software Construction\Project\ESC\Samples\testGDB1.gdb"
#st_size: tell the file size by byte    FileNotFoundError: null file

def file_is_empty(file_path):
    return os.stat(file_path).st_size == 0
is_empty = file_is_empty(file_path)
try:
    is_empty == True
except FileNotFoundError:
    print("we can't find files at your directory, please redo")
else:
    print("your file selected is blank, please redo")