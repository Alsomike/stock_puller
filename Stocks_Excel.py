import openpyxl as xl
import time

trial_stocks = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5']
trial_prices = ['price1', 'price2', 'price3', 'price4', 'price5']

SR_wb = xl.load_workbook('\\Users\\mpell\\OneDrive\\Documents\\PythonProjects\\Git\\Stock_Records.xlsx')
#loads excel file using where it lies in the directory
SR_Sheet = SR_wb["Sheet"]
#finds sheet names "Sheet" in wb and gives it a python element names SR_Sheet
now = time.strftime("%x")
#establishes variable now that gives us the current date
SR_Sheet['A1'].value = now
#adds the current date to the first cell 
SR_wb.save('Stock_Records.xlsx')
#saves changes made to excel file

