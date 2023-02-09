# date : 2023-02-06
# author : Lani Jeong
# desc : 윈도우 창닫기 앱 + 툴팁
import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):     # signal slot
        btn = QPushButton('Be Happy', self)
        btn.move(310, 170)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('Just Do It! <b>Bye:):')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./Day09/smile-hand-drawn-emoticon.png'))
        self.setWindowTitle('SMILE')
        self.setGeometry(800, 400, 400, 200)    # x, y, w, h
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
