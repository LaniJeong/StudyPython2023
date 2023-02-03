# date : 2023-02-03
# author : Lani Jeong
# desc : urllib 패키지 불러오기          # internet: request and response about network
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')   # htps : http security
res = urlopen(req)                       # urlopen: 함수
print(res.status)



