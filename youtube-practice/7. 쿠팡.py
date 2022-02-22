import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.coupang.com/np/search?q=헤드폰&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
# 유저인척하려면 유저에이전트가 필요함. 이거없으니까 크롤링이 안됨.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}
res = requests.get(url=url, headers=headers)

soup = BeautifulSoup(res.text, features='lxml')

products = soup.find_all('li', attrs={'class': re.compile('^search-product')})

for i in products:
    product_title = i.find('div', attrs={'class': 'name'}).getText()
    price = i.find('strong', attrs={'class':'price-value'}).getText()
    print(product_title)
    print(price)
