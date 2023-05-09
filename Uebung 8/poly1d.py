"""import matplotlib.pyplot as plt
import numpy as np
f = np.poly1d([1,2,3,4])
x = np.linspace(-10,10,60)
y = f(x)
plt.plot(x,y,'ko-')
plt.show()"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Uebung 8/polynom.ui", self)
        self.show()
        layout = QVBoxLayout()
        figure = plt.figure(figsize=(16, 9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas)
        self.QPushButton.clicked.connect(self.plot)
        #self.QLineEdit_2.textChanged.connect(self.update_wertebereich)
        #self.QLineEdit_3.textChanged.connect(self.update_wertebereich)
        #self.QLineEdit_4.textChanged.connect(self.update_wertebereich)
        self.farbenComboBox.currentText.connect(self.farbe_zuweisen)

        layout.addWidget(self.canvas)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.lineEdit_3)
        layout.addWidget(self.lineEdit_4)
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

    def plot(self):
        plt.clf()
        werte = self.lineEdit.text()
        wertmin = self.lineEdit_2.text()
        wertmax = self.lineEdit_3.text()
        anzPkt = self.lineEdit_4.text()
        farbe = f"{self.farbe}o-"
        x = np.linspace(wertmin, wertmax, anzPkt)
        f = np.poly1d([werte])
        y = f(x)
        plt.plot(x, y, farbe)
        plt.axis("equal")
        self.canvas.draw()

    def update_wertebereich(self):
        pass

    def farbe_zuweisen(self, value):
        if value == "schwarz":
            self.farbe = "k"

        elif value == "blau":
            self.farbe = "b"

        elif value == "rot":
            self.farbe = "r"

        elif value == "grün":
            self.farbe = "g"

        elif value == "violett":
            self.farbe = "v"



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec()

