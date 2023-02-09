import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
       
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
    
    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit. setShortcut('Ctrl+Q')  # 단축키 지정
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')   # 툴바타이틀은 없어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate()    # 현재 일자
        time = QTime.currentTime()   # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd')+ ' ' + time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/smile-hand-drawn-emoticon.png'))
        # GUI 화면 설정
        self.setWindowTitle('SMILE')
        # self.move(200, 200)       # 창이 뜨는 위치 (1440 // 2, 900 // 2) -> 정중앙에 위치
        self.resize(400, 200)       # 창의 크기
        self.setCenter()            # 창의 중심에
        self.show()                 # 핵심

    # 화면 중심 세팅
    def setCenter(self):
        qr = self.frameGeometry()   # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()   # 모니터화면 중심
        qr.moveCenter(cp) 
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    