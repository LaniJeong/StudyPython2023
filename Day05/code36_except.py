# date : 2023-02-03
# author : Lani Jeong
# desc : 예외처리(Exception)
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()

# 원시적 예외처리
# if y == 0:                          # 예외를 빠져나갈 방법
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x, y))                    # 0을 넣었을 경우 error라고 뜨지만 exception이다.
# except ZeroDivisionError as e:        # 굳이 exception을 나누지 않아도 됨 / 문자 추가 시 사용
#     print('0으로 나누면 안되요!')
except Exception as e:                  # 예외를 알려줌 -> 모든 예외처리 중 마지막으로 작성하기
    print(e)
    exit()
finally:                                # 어떻게든 일을 처리하게 함 / 이거 실행 뒤 종료
    print('계산은 계속됩니다.')


print(add(x, y))
print(mul(x, y))

