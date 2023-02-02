# date : 2023-02-02
# author : Lani Jeong
# desc : 객체지향
## 클래스 생성
class Person:
    #pass                # pass : 뭘 적어야 할 지 모를 때 (오류안남)
    name = '익명'        # 속성변수(속변) : class의 변수
    height = ''
    gender = ''
    blood_type = 'O'

    def walk(self):      # def에 self를 써야함
        print('걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print('멈춥니다.')

lani = Person()          # instance: 만들어진 객체
lani.name = '정수민'
lani.height = '160'
lani.gender = 'F'
lani.blood_type = 'Rh+ O'

print(f'{lani.name}의 혈액형은 {lani.blood_type}입니다.')
print(f'{lani.name}의 키는 {lani.height}입니다.')
print(f'{lani.name}의 성별은 {lani.gender}입니다.')

lani.run('Fast')
