import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Smile:)')
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/smile-hand-drawn-emoticon.png'))
        # self.move(200, 200)  # 창이 뜨는 위치 (1440 // 2, 900 // 2) -> 정중앙에 위치
        self.resize(400, 200)  # 창의 크기
        self.show()            # 핵심

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    