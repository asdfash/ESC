import pandas as pd

def import_excel(excelpath):
    column_list = []
    data_column = pd.read_excel(excelpath, 'For Sharing').columns
    for i in data_column:
        column_list.append(i)
    converter = {col: str for col in column_list} 
    data = pd.read_excel(excelpath, converters=converter) #read the dataframe as str datatype
    return data

