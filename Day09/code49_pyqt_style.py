# style
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet('color: red;'
                              'border-style: solid;'     #직선
                              'border-width: 5px;'
                              'border-color: #FA8072;'
                              'border-radius: 10px')     # 모서리 둥글게
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet('color: green;'
                              'border-style: dashed;'    # 점선
                              'border-width: 5px;'
                              'border-color: #7FFFD4;'
                              'border-radius: 10px')

        vbox = QHBoxLayout()      # 레이아웃 세로 구분짓는 레이아웃  / VBox: 가로배열  /  HBox: 세로배열
        vbox.addWidget(lbl_red)   # 위젯 추가
        vbox.addWidget(lbl_green)

        self.setLayout(vbox)      # 전체 레이아웃에 vbox를 추가
        

        # 기본설정 - 사이즈, show() 필수
        self.setWindowTitle('스타일 지정')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())