from matplotlib.pyplot import scatter, show
from pandas import DataFrame
from re import match, split
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

xm = urlopen('https://www.mi.com/').read()
xmsoup = BeautifulSoup(xm, "lxml")
xmall = xmsoup.find_all(class_=['title', 'price'])
xmALL = split(
    r'</p>, <div class="title">|</div>, <p class="price">|<div class="title">', str(xmall))
for i in range(len(xmALL)):
    if(xmALL[i] == '小米11 Ultra'):
        xmprice = match(r'\d*', xmALL[i+1]).group()
        break
header = {
    'user-agent': r'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36 Edg/91.0.864.41'}
requests = Request(
    'https://search.jd.com/search?keyword=%E5%B0%8F%E7%B1%B311%20Ultra&qrst=1&wq=%E5%B0%8F%E7%B1%B311%20Ultra&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&cid3=655', headers=header)
jd = urlopen(requests).read()
jdsoup = BeautifulSoup(jd, "lxml")
jdall = jdsoup.find_all(class_='p-price')
jdALL = split(r'<i>|</i>', str(jdall))
jdprice = []
i = 1
while(i < len(jdALL)):
    jdprice.append(jdALL[i])
    i += 2
jdall = jdsoup.find_all(class_='p-shop')
jdALL = split(
    r'data-reputation="|" data-score="|" data-selfware="', str(jdall))
jdreputation = []
jdscore = []
i = 1
while(i < len(jdALL)):
    jdreputation.append(jdALL[i])
    i += 1
    jdscore.append(jdALL[i])
    i += 2
price = DataFrame()
price['京东'] = jdprice
price['小米'] = xmprice
scatter(price)
show()