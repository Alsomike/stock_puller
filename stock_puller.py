import requests
import bs4

stock = []
def getStock(i):
	res = requests.get(i)
	soup = bs4.BeautifulSoup(res.text)
	stock = soup.select('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)')
	stockprint = stock[0].text.strip()
	print('$' + stockprint)

stockticker = input("what is the ticker? ")

getStock('https://finance.yahoo.com/quote/' + stockticker + '?p=TSLA&.tsrc=fin-srch')

