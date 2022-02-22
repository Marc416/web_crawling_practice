import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='lxml')
# 클래스가 title인 모든 'a'태그 앨리먼트들이 반
cartoons = soup.find_all('a', attrs={'class': 'title'})

# 네이버 웹툰 전체 목록가져오기
for i in cartoons:
    print(i.get_text())
