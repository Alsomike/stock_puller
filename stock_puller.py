import requests
import bs4

UserInput = 0
StockPrice = []
StockTicker = []
def getStock(i):
	res = requests.get(i)
	soup = bs4.BeautifulSoup(res.text, features="html.parser")
	HTMLSelector = soup.select('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)')
	stockprint = HTMLSelector[0].text.strip()
	StockPrice.append(stockprint)
	print('$' + stockprint)
while UserInput != 1:
	UserInput = input("what is the ticker? ")
	StockTicker.append(UserInput)
	getStock('https://finance.yahoo.com/quote/' + UserInput + '?p=TSLA&.tsrc=fin-srch')
	print(StockTicker, StockPrice)




#use for loop to add len of list with prices to excel sheet
#want it to loop through *stock* list in order to 