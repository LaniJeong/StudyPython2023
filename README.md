# StudyPython2023
부경대 IoT 파이썬 학습 리포지토리


## 1일차
1.  기본 구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치

2. Python 기본
    - 콘솔출력
    - 주석

```python
# desc : 콘솔출력 -> 주석
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자

```python
# 변수
val = 1

# 자료형
print(type(val))  # <class 'int'>

# 문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.')         # 파이는 3.121592입니다.
print(f'파이는 {pi:0.02f}입니다.')   # 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')    # 파이는        3.142입니다.
```

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수
    
## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 oop
        * 객체(object) : 전체나 집단에 상대하여 하나하나의 낱개를 이르는 말. 독립적인 것.
        * 동사와 명사의 집합 / 명사: 변수 / 동사: 함수 / class: 만들어 주는 틀
    - 패키지, 모듈

## 5일차
1. 파이썬 기본
    - 패키지 계속
    - 입출력 다시
    - 예외처리
    ```python
    except Exception as e:                  # 예외를 알려줌 -> 모든 예외처리 중 마지막으로 작성하기
    print(e)
    ```
    - 객체지향 다시

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
     - 객체지향 다시
         - 객체지향 특징
        - 상속, 다중 상속
2. 파이썬 응용
    - 주소록 프로그램 만들기 [소스](https://github.com/LaniJeong/StudyPython2023/blob/main/Project/address_app.py)
![실행화면](https://raw.githubusercontent.com/LaniJeong/StudyPython2023/main/images/address_app.png)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성  / 파일 -> 새파일
        - m : markdown  /  y : python  (esc로 빠져 나온 후 사용)
        - ctrl + enter : 실행
        - a : 앞에 셀 만들기  /  b : 뒤에 셀 만들기
        - debugging(Ctrl + Shift + Alt + Enter) : 위의 셀로 이동하지 않을 경우 py로 내보내기 후 dubugging
    - 리스트 연산 추가
    - 자료구조 추가
    - library 사용법
    - 윈폼 개발(GUI)
    - 응용 학습

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹 크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터 포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링

![실행화면] (file:///C:/source/StudyPython2023/images/jupyter_folium.png)
Folium OpenAPI 연동화면

## 9일차
1. 파이썬 응용
    - GUI 개발(PyQt)
    - 자료구조 추가


