from re import search, split, sub
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from matplotlib.pyplot import bar, scatter, show, title
from pylab import mpl

header = {
    'user-agent': r'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36 Edg/91.0.864.41'}
requests = Request(
    'https://search.jd.com/Search?keyword=%E5%B0%8F%E7%B1%B311&qrst=1&wq=%E5%B0%8F%E7%B1%B311&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&pvid=4f1bd0efbe2c4a17ad3119e4087e1d6f&page=1&s=1&click=1', headers=header)
jd = urlopen(requests).read()
jdsoup = BeautifulSoup(jd, "lxml")
jdall = jdsoup.find_all(class_=[
                        'p-price', 'p-name-type-2', 'curr-shop hd-shopname', 'gl-item'])
jdALL = split(
    r'<i>|</i>|<li class="gl-item" data-sku="|" data-spu="', str(jdall))
jdprice = []
shopname = []
sku = []
i = 3
while(i < len(jdALL)-11):
    if(search(r'<font class="skcolor_ljg">小米11</font> 5G', jdALL[i+1]) and search(r'^[0-9]*$', jdALL[i-2])):
        sku.append(jdALL[i-2])
        jdprice.append(float(jdALL[i]))
        j = 4
        while(True):
            jdALL2 = split(r'>|<', jdALL[i+j])
            if(len(jdALL2) > 6):
                if(search(r'^[\u4e00-\u9fa5]{1,}$', jdALL2[6])):
                    shopname.append(jdALL2[6])
                    i += 8
                    break
            j += 1
    i += 1

requests = Request(
    'https://search.jd.com/Search?keyword=%E5%B0%8F%E7%B1%B311&qrst=1&wq=%E5%B0%8F%E7%B1%B311&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&pvid=4f1bd0efbe2c4a17ad3119e4087e1d6f&page=3&s=59&click=1', headers=header)
jd = urlopen(requests).read()
jdsoup = BeautifulSoup(jd, "lxml")
jdall = jdsoup.find_all(class_=[
                        'p-price', 'p-name-type-2', 'curr-shop hd-shopname', 'gl-item'])
jdALL = split(
    r'<i>|</i>|<li class="gl-item" data-sku="|" data-spu="', str(jdall))
i = 3
while(i < len(jdALL)-11):
    if(search(r'<font class="skcolor_ljg">小米11</font> 5G', jdALL[i+1]) and search(r'^[0-9]*$', jdALL[i-2])):
        sku.append(jdALL[i-2])
        jdprice.append(float(jdALL[i]))
        j = 4
        while(True):
            jdALL2 = split(r'>|<', jdALL[i+j])
            if(len(jdALL2) > 6):
                if(search(r'^[\u4e00-\u9fa5]{1,}$', jdALL2[6])):
                    shopname.append(jdALL2[6])
                    i += 8
                    break
            j += 1
    i += 1

requests = Request(
    'https://search.jd.com/Search?keyword=%E5%B0%8F%E7%B1%B311&qrst=1&wq=%E5%B0%8F%E7%B1%B311&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&pvid=4f1bd0efbe2c4a17ad3119e4087e1d6f&page=5&s=116&click=1', headers=header)
jd = urlopen(requests).read()
jdsoup = BeautifulSoup(jd, "lxml")
jdall = jdsoup.find_all(class_=[
                        'p-price', 'p-name-type-2', 'curr-shop hd-shopname', 'gl-item'])
jdALL = split(
    r'<i>|</i>|<li class="gl-item" data-sku="|" data-spu="', str(jdall))
i = 3
while(i < len(jdALL)-11):
    if(search(r'<font class="skcolor_ljg">小米11</font> 5G', jdALL[i+1]) and search(r'^[0-9]*$', jdALL[i-2])):
        sku.append(jdALL[i-2])
        jdprice.append(float(jdALL[i]))
        j = 4
        while(True):
            jdALL2 = split(r'>|<', jdALL[i+j])
            if(len(jdALL2) > 6):
                if(search(r'^[\u4e00-\u9fa5]{1,}$', jdALL2[6])):
                    shopname.append(jdALL2[6])
                    i += 8
                    break
            j += 1
    i += 1
page = 7
s = 176
while(page <= 19):
    requests = Request(
        'https://search.jd.com/Search?keyword=%E5%B0%8F%E7%B1%B311&qrst=1&wq=%E5%B0%8F%E7%B1%B311&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&pvid=4f1bd0efbe2c4a17ad3119e4087e1d6f&page='+str(page)+'&s='+str(s)+'&click=1', headers=header)
    jd = urlopen(requests).read()
    jdsoup = BeautifulSoup(jd, "lxml")
    jdall = jdsoup.find_all(
        class_=['p-price', 'p-name-type-2', 'curr-shop hd-shopname', 'gl-item'])
    jdALL = split(
        r'<i>|</i>|<li class="gl-item" data-sku="|" data-spu="', str(jdall))
    i = 3
    while(i < len(jdALL)-11):
        if(search(r'<font class="skcolor_ljg">小米11</font> 5G', jdALL[i+1]) and search(r'^[0-9]*$', jdALL[i-2])):
            sku.append(jdALL[i-2])
            jdprice.append(float(jdALL[i]))
            j = 4
            while(True):
                jdALL2 = split(r'>|<', jdALL[i+j])
                if(len(jdALL2) > 6):
                    if(search(r'^[\u4e00-\u9fa5]{1,}$', jdALL2[6])):
                        shopname.append(jdALL2[6])
                        i += 8
                        break
                j += 1
        i += 1
    page += 2
    s += 60

requeststr = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='
for i in sku:
    requeststr += i+','
requeststr += '&callback=jQuery1100191&_=1623928017599'
requests = Request(requeststr, headers=header)
js = urlopen(requests).read()
jssoup = BeautifulSoup(js, "lxml")
jsall = split(r'"CommentCountStr":"|","CommentCount"', str(jssoup))
sales = []
i = 1
while(i < len(jsall)):
    sales.append(jsall[i])
    i += 2
for i in range(len(sales)):
    sales[i] = sub('万', '0000', sales[i])
    sales[i] = sub('\+', '', sales[i])
    sales[i] = int(sales[i])

mpl.rcParams['font.sans-serif'] = ['simhei']
bar(shopname, sales)
title('销量')
show()
scatter(shopname, jdprice)
title('价格')
show()

maxIndex = 0
for i in range(len(sales)):
    if(sales[i] > sales[maxIndex]):
        maxIndex = i
max = jdprice[maxIndex]
print(jdprice[maxIndex])
print(shopname[maxIndex])
jdprice.sort()
print(jdprice.index(max))
print('最低价格：', jdprice[0])
