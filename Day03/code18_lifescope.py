# date : 2023-02-01
# author : Lani Jeong
# desc : 함수
## 라이프 스코프
a = 1           # 전역변수

def vartest(x): # 지역변수, def 안에서만 작용 / 함수 호출 시 적용
    global a    # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다
    x = x + 1
    return x

a = vartest()
print(a)