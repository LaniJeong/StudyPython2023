# date : 2023-02-01
# author : Lani Jeong
# desc : 함수
## 람다함수 -> 한번쓰고 버리는 함수
def add(x, y):
    return x + y

print(add(7, 4))

# 람다 함수로 쓰면
print((lambda x, y: x+y)(7, 4))

# 지금은 어려우니까 나중에