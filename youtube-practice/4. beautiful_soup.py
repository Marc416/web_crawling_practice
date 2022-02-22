import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='lxml')
# print(soup.div.get_text().split())
# print(soup.a['href'])


rank1 = soup.find('li', attrs={'class': 'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling.get_text())
for i in rank1.find_next_siblings('li'):
    print(i.get_text())

"""
lxml -> xml 파서
soup -> 파싱된 태그에 대한 컨트롤러
"""
