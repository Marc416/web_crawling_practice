import requests

url = 'http://google.com'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

res = requests.get(url,headers=headers)
# print(res.raise_for_status())

with open('nadocoding.html', 'w', encoding='utf8') as f:
    # if f is None:
    f.write(res.text)

"""
UserAgent : 브라우저별 UI 렌더를 도와주는 역할
"""
