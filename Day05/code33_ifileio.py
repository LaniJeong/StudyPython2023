# date : 2023-02-03
# author : Lani Jeong
# desc : IO(input/output)
## 파일 만들기
file = open('sample.txt', 'w') # 파일 쓰기로 만듦

file.write('hi 안녕')
file.write('wow first file')

file.close()
print('sample.txt가 생성되었습니다.')

# ASCII -> 한단어를 표현하는 체계(영어)
