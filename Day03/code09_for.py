# date : 2023-02-01
# author : Lani Jeong
# desc : 흐름제어
## for문을 배워요
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(item)
    sum += item           # += : sum = sum + item

print('합계는 ', sum)

# 리스트를 편하ㅏ게 만드는 방법
vals = [i for i in range(1,11)]   # 원하는 숫자 +1해야함
print(vals)

# continue / break  -> for문에서만 사용가능
num = 0
for item  in vals:
    num += 1
    if num % 2 == 0:     # % : 나누고 난 후 나머지
        #continue        # 이후의 것을 수행하지 않고 다시 for문으로 감
        break            # break를 만나면 for문을 완전히 탈출
    else:
        print(num, '번 수는', item, '입니다.')

