# date : 2023-02-01
# author : Lani Jeong
# desc : 흐름제어
## if문을 배워요
name = '창균'
state = '아픔'

if name == '수민':                                  # == : 같다 / != : 같지 않다
    print('진료실에서 담당의사를 만납니다.')
    if state == '아픔':
        print('선생님, 아파요..')
        print('어디가 아프신가요?')
        print('선생님, 배가아파요.')
        print('배 어디가 어떻게 아프십니까?')
    else:
        print('어디가 아프십니까?')
        print('안아파요.')
        print('그럼 왜 오셨나요?')


elif name == '창균':                                # elif : 또 다른 조건 사용시
    print('주사실로 갑니다.')
    print('바지를 내리세요.')
else: 
    print('기다립니다.')



