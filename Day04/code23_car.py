# date : 2023-02-02
# author : Lani Jeong
# desc : 객체지향
## 자동차 클래스
class Car:
    __number = '98나 0909'

    def get_number(self):                    # -> str : 생략가능
        return self.__number

    def set_number(self):
        return self.__number

    #클래스 외부에선 변경X
    def __init__(self, number='54라 9538') -> None:
       self.__number = number
       print('__init__')                    # 생성자 / 많이 씀

    # def __new__(cls):
    #     print('__new__')                     # 새로운 class 생성자 / 잘 안씀
    #     return super().__new__(cls)          # 부모클래스(상속)

    def __str__(self) -> str:                # str : 객체이름을 넣어 프린트 할 때
        return f'차번호는 {self.__number}'

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999'  # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는 피아제고 번호가 {mycar.get_number()} 에요.')

mycar.number = '132거 8874'
print(mycar.number)




    
