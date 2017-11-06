# https://openpyxl.readthedocs.io/en/default/usage.html#read-an-existing-workbook

from openpyxl import load_workbook
wb = load_workbook(filename = 'empty_book.xlsx')
sheet_ranges = wb['Pi']
print(sheet_ranges['D18'].value)