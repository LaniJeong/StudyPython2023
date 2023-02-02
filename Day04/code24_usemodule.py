# date : 2023-02-02
# author : Lani Jeong
# desc : 모듈사용
import math as m                      # as m : m이라는 별명 부여(math 실행 안됨) / 클래스로 안된 모듈
import code22_person as p             # 우리가 만든 클래스
from code23_car import Car

# 
print('==================')
print(m.pi)

print(m.cos(0))
print(m.ceil(3.8))                    # ceil : 올림 / floor : 내림
print(2 ** 10)
print(m.pow(2, 10))                   # pow : 소숫점까지 나옴

# 우리가 만든 모듈 사용
me = p.Person('임창균', 176, '남성')
print(me)

#
mycar = Car()
print(mycar)
