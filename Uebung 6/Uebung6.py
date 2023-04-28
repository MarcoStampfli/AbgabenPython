from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.QtWebEngineWidgets import *


class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        laenge = self.l_LineEdit.text()
        breite = self.breiteLineEdit.text()
        url = QUrl(f"https://www.google.ch/maps/place/{laenge},{breite}")
        QDesktopServices.openUrl(url)




app = QApplication([])
win = UIFenster()
app.exec()