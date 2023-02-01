# date : 2023-02-01
# author : Lani Jeong
# desc : 흐름제어
## 구구단 프로그램
for x in range(2, 10):
    print(f'{x}단 시작 =======')
    for y in range(1, 10):
        print(f'{x} X {y} = {x*y:>2}', end=' ')   # end=' ' : 여러줄로 나눠지게 하지 않고 이어지게 함  / :>2 : 2줄로 만들고 오른쪽 정렬
        # print(x, 'x', y, '=', x*y)
    print()                                       # 나눠주기


