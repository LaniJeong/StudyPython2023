# date : 2023-01-31
# author : Lani Jeong
# desc : 자료형

## None : 값이 없는 값
None # don't know

print(None)
print(0 == None)
print('' == None)

## 숫자형
# type()은 자료형을 반환하는 파이썬 내장함수
val = 3
print(type(val))

val = 'Hello'
print(type(val))

val = 0b1010
print(type(val))

val = 12.595664668653248621896658654
print(type(val))

# 숫자를 쓸 때 ,대신 _사용(보기편하게)
val = 4_520_000
print(val)

val = 3_099.99
print(val)

## 문자열형
val = 'Life is short, you need Python'
print(val)
print(type(val))

# \n : 엔터와 같은 기능(한 줄 내리기) / 탈출문자
val = 'Hell \nWorld!'
print(val)
# \t : 4칸정도 띄움
val = 'Hell \tWorld!'
print(val)
# \b : 한 칸 들여쓰기
val = 'Hell \t\bWorld!'
print(val)
# '''  ''' : 문장 길게 쓰기
val = '''Life is short,
You need Python'''
print(val)
val = "Hi, I'm 'Lani'"
# ' ' 안에 ' '를 쓸 수 없어 \'로 작성
val = 'Hi, I\'m \'Lani\''

## 불린형(불형 True or False)
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
# is는 앞 뒤가 같은지
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(3)) # 0이 아니면 다 참 / 1 이외의 값은 True라고 하지않음

