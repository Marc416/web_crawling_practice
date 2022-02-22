import requests

res =requests.get('http://naver.com')

print(res.status_code)

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)