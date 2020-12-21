import openpyxl as xl
import time

trial_stocks = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5']
trial_prices = ['price1', 'price2', 'price3', 'price4', 'price5']

SR_wb = xl.load_workbook('\\Users\\mpell\\OneDrive\\Documents\\PythonProjects\\Git\\Stock_Records.xlsx')
SR_Sheet = SR_wb["Sheet"]

SR_Sheet = SR_wb['Sheet']
now = time.strftime("%x")
SR_Sheet['A1'].value = now

SR_wb.save('Stock_Records.xlsx')


