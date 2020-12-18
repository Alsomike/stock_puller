import openpyxl

wb = openpyxl.load_workbook("Stock_Records.xlsx")

sheet = wb.active

cell = sheet.cell(row = 1, column = 1)

print(cell)