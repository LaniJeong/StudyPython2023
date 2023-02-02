# date : 2023-02-02
# author : Lani Jeong
# desc : 객체지향
## 클래스 생성   - 클래스의 실체: instance
class Person: 
    #pass                                      # pass : 뭘 적어야 할 지 모를 때 (오류안남)
    name = '익명'                              # 속성변수(속변) : class의 변수
    height = ''
    gender = ''
    blood_type = 'O'

    # 1. 생성자 추가
    # def __init__(self):                        # __init__ : 초기화 하겠다는 말 / -> None : 없어도 됨
    #     self.name = '홍길동'                   # name : 함수의 매개변수
    #     self.height = '170' 
    #     self.gender = 'M'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'M') -> None:   # 사용여부에 따라 변수의 글씨 색이 달라짐  / parameter기본값 지정
        self.name = name
        self.height = height
        self.gender = gender

        

    def walk(self):                            # def에 self를 써야함
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가)멈춥니다.')

    # 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:                                           # str로 문자열을 return해야함 
         return f'출력 : 이름은 {self.name}, 성별은 {self.gender} '     # str을 쓰지 않을 때 : <__main__.Person object at 0x000001B018E21190> 코드가 나옴


lani = Person('정수민', 160, 'F')                                       # instance: 객체 생성 (함수를 만들어라)
#lani.name = '정수민'
#lani.height = '160'
#lani.gender = 'F'
#lani.blood_type = 'Rh+ O'

print(f'{lani.name}의 혈액형은 {lani.blood_type}입니다.')
print(f'{lani.name}의 키는 {lani.height}입니다.')
print(f'{lani.name}의 성별은 {lani.gender}입니다.')

lani.run('Fast')

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)

print('====================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('ashely', 165, 'F')  # 클래스 객체 생성자
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
