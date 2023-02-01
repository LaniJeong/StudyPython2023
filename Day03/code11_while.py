# date : 2023-02-01
# author : Lani Jeong
# desc : 흐름제어
## while문
hit = 0                                   # 변수 초기화

while hit < 11:                           # True를 넣으면 무한반복
    hit += 1                              # hit를 1씩 증가

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print('나무가 넘어갔습니다!')
        break                             # while 을 빠져나감
    else:
        print('나무가 아직 넘어가지 않았습니다.')

print('나무찍기 완료')