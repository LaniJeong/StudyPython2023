import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
       
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit. setShortcut('Ctrl+Q')  # 단축키 지정
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 상태바
        self.statusBar().showMessage('StatusBar message')
        # GUI 화면 설정
        self.setWindowTitle('SMILE')
        # self.move(200, 200)  # 창이 뜨는 위치 (1440 // 2, 900 // 2) -> 정중앙에 위치
        self.resize(400, 200)  # 창의 크기
        self.show()            # 핵심



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    