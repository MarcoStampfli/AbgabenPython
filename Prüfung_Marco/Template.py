#Aufgabe......

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from csv import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("QHBoxLayout Demo")

        # Gui Elenemente Layout erstellen:
        layout = QHBoxLayout() #horizontal Layout
        #layout = QVBoxLayout() #vertikal Layout
        #layout = GridboxLayout() #raster Layout
        #layout = QFormLayout() #Wie GridLayout, muss aber Label nicht zusätzlich machen.



        # Gui Elenemente Push-Buttons erzeugen:
        button1 = QPushButton("Hello")
        button2 = QPushButton("PyQt5")
        button3 = QPushButton("World")

        # Buttons dem Layout hinzufügen
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)



        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)
        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)
        # Fenster anzeigen
        self.show()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()
