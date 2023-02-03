# date : 2023-02-03
# author : Lani Jeong
# desc : IO(input/output)
## 다중입력
# x, y, z = input('세 영단어를 입력하세요. > ').split()  # .split : 자르기

# print(x)
# print(y)
# print(z)

## 완전 다중입력(갯수가 몇개든 상관없음)
inputs = list(map(str, input('단어를 입력하세요. > ').split()))     # str : 글자를 받을 때

print(inputs)

inputs = list(map(int, input('정수를 입력하세요. > ').split()))     # int : 숫자를 받을 때

print(inputs)

