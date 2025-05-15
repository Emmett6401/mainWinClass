from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from pyQTapp04 import myWindow

Form, Window = uic.loadUiType("res/mainWindow.ui")

class MainWindow:
    def __init__(self):
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.fb_window = myWindow()  # myWindow 인스턴스 생성

        # 메뉴 액션 연결
        self.form.actionMini_FaceBook.triggered.connect(self.fb_window.lounch)
        self.form.actionITEDU.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://itedu.wsu.ac.kr")))
        self.form.actionWSU.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.wsu.ac.kr")))

    def lounch(self):
        self.window.show()

if __name__ == "__main__":
    app = QApplication([])
    mw = MainWindow()
    mw.lounch()
    app.exec()