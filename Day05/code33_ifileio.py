# date : 2023-02-03
# author : Lani Jeong
# desc : IO(input/output)
## 파일 만들기
file = open('../sample06.txt', 'w', encoding='utf-8')        # 파일 쓰기로 만듦  / encoding='utf-8' : 모든 언어 수용
# \\두번 넣거나 앞에 f를 붙임, /도 사용가능

file.write('hi 안녕 \n')                                                    # \n : 줄바꿈
file.write('wow second file \n')
file.write('절대경로에 파일 생성! \n')

file.close()
print('sample05.txt가 생성되었습니다.')

# 글자 incording
# ASCII -> 한단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능


## 파일/폴더 경로
# 절대경로 : C:\DEV\Temp\Bank\sample01.txt / 모든 경로 다 작성
# 상대경로 : ./Day05/../Day04/sample06.txt / . : 현재위치 .. : 상위폴더


