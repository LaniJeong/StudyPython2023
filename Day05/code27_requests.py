# date : 2023-02-03
# author : Lani Jeong
# desc : 외부 패키지 사용
import requests

res = requests.get('https://www.naver.com')
print(res.status_code)
print('====================')
print(res.content)