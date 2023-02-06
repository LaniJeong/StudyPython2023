# date : 2023-02-06
# author : Lani Jeong
# desc : 콘솔출력 보충
## 이스케이프 캐릭터(탈출문자)
print('1.Hello.\r\nWorld')   
print('2.Hello.\nWorld')            # \n : 다음줄로(권장)

print('3.Hello.\n\tWorld')          # \t : tab
print('4.Hello.\n\t\bWorld')        # \b : back space

print('5.Hello.\n \'World\'')       # \' : 문자열내 '표시
print('6.Hello.\n"World"')          
print('7.Hello.\"World\"')          # \"" : 문자열내 ""표시

print('8.Hello. \ World')           # \\ : \ 문자열에 표현(python은 \도 가능)
print('9.Hello\0')                  # \0 : 문자열의 끝을 알려줌

# 문자열 포맷팅 - old ver.
# %로 포맷코드를 시작
me = '저'
name = '정수민'
age = 20
print('%s는 %s입니다. %d대 입니다.'%(me, name, age))  # %s : 문자열 / %d : 정수

print(f'{2455.1235135:.2f}')        # new ver. .nf : 소숫점 이후 숫자 n개

print('%4.4f' %(2455.1235135))      # %n.m : 전체길이n개, 소숫점 m개


