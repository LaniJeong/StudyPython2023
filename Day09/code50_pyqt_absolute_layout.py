# 레이아웃 절대적배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init_(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lable1 = QLabel('Lable1', self)
        lable1.move(20, 20)
        lable1 = QLabel('Lable2', self)
        lable1.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)

        # 필수설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())