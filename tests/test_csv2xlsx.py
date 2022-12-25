import sys
sys.path.insert(0, './src')
import runpy
import openpyxl
from Converter import Converter

def test_get_output_filename_with_extension():
    assert './data/something.xlsx' == (Converter('./data/something.input')).get_output_filename('xlsx')

def test_get_output_filename_without_extension():
    assert './data/something.xlsx' == (Converter('./data/something')).get_output_filename('xlsx')

def test_get_input_extension_with_extension():
    assert '.xlsx' == (Converter('./data/something.xlsx')).get_input_extension()

def test_get_input_extension_without_extension():
    assert '' == (Converter('./data/something')).get_input_extension()

# def  test_check_xlsx_fields_after_conversion():
#     m = runpy.run_path('./src/csv2xlsx.py', )
#     m['main']('','./tests/data/orlenpaczka.csv')

#     # Open Workbook
#     wb = openpyxl.load_workbook(filename='./tests/data/orlenpaczka.xlsx', data_only=True)

#     # Get All Sheets
#     a_sheet_names = wb.get_sheet_names()
#     print(a_sheet_names)

#     # Get Sheet Object by names
#     o_sheet = wb.get_sheet_by_name("Sheet1")
#     print(o_sheet)

#     # Get Cell Values
#     o_cell = o_sheet['A1']
#     print(o_cell.value)

#     o_cell = o_sheet.cell(row=2, column=1)
#     print(o_cell.value)

