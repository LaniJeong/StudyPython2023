# date : 2023-02-06
# author : Lani Jeong
# desc : 주소록앱
import os               # 운영체제용 모듈

class Contact:
    ## 2. 생성자 - 이름, 전번, 이메일, 주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    ## 4: __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이    름 : {self.__name}\n'
                   f'핸 드 폰 : {self.__phone_num}\n'
                   f'이 메 일 : {self.__email}\n'
                   f'주    소 : {self.__addr}\n')
        return str_res

## 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름/전번/이메일/주소)').split('/')
    # print(name, phone_num, email, addr)
    ## 7. Contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)   #(addr = addr, email = email ,,,) 이런식으로도 작성 가능
    return contact

## 추가. 화면 클리어
def clear_console():
    command = 'clear'               # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'):    # Window 운영체제라면
        command = 'cls'             # 윈도우 화면 클리어 명령어

    os.system(command)

## 6. 메뉴표시
def get_menu():
    str_menu = '''주소록앱 v0.5
                  1. 연락처 추가
                  2. 연락처 출력
                  3. 연락처 삭제
                  4. 앱종료'''
    print(str_menu)
    menu = int(input('메뉴입력 : '))
    return menu

## 3. 전체 실행
def run():
    contacts = list()  # 주소를 담기 위한 빈 리스트 생성
    # temp = Contact('임창균', '010-1996-0126', 'mx0514@naver.com',
    #                 '서울특별시 강남구')
    # set_contact()
    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:               ## 8. 연락처 추가
            clear_console()
            contact = set_contact()
            contacts.append(contact)
        elif sel_menu == 4:
            break
        else:
            clear_console()
        

## 1.
if __name__ == '__main__':
    # print('주소록앱 시작합니다')
    run()

