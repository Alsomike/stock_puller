import openpyxl

wb = openpyxl.load_workbook('Stock_Records.xlsx')

sheet = wb.get_sheet_names('Sheet')
sheet['A1'].value == None
