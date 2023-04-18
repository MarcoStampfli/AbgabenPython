import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("Währungsrechner")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        chfLineEdit = QLineEdit()
        euroLineEdit = QTextEdit()
        chf = QAction(chfLineEdit)
        
        button = QPushButton("Umrechnen")
        button.clicked.connect(self.umrechnen)

        # Layout füllen:
        layout.addRow("Schweizerfranken", chfLineEdit) #String = Labelname
        layout.addRow("Euro", euroLineEdit)
        
        layout.addRow(button)

   

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def umrechnen(self)-> float:
        return self * 0.876

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()