from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests 

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

class Content:
    def __init__(self, url, price):
        self.url = url
        self.price = price

def get_page(url):
    req = requests.get(url) 
    if req.status_code == 200:
        return BeautifulSoup(req.text, 'html.parser')
    return None

def get_data(url):
    bs = get_page(url)
    if bs is None:
        return bs
    price = bs.find("span", {"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    return Content(url, price)

content = get_data(url)
if content is None:
    print('ERROR!')
else:
    print('Price: {}'.format(content.price))
