# date : 2023-02-03
# author : Lani Jeong
# desc : IO(input/output)
# 파일 읽어오기
file = open('./Day05/sample05.txt', 'r', encoding='utf-8')


text = file.readline()
print(text)

while True:
     text = file.read()
    
     if not text: break

     print(text)

file.close()                # open 하면 무조건 close

