import sys
from PyQt5.QtWidgets import *
import csv

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("GUI Programierung - Adresserfassung")

        # Layout erstellen:
        layout = QFormLayout()
        #layoutmenu = QFormLayout()

        #Menu-Bar erstellen
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        

        save = QAction("Save", self)
        filemenu.addAction(save)
        filemenu.addSeparator()
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        filemenu.addAction(quit)
        quit.triggered.connect(self.menu_quit)
        
        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.emailLineEdit = QLineEdit()
        self.ageCalendarWidget = QCalendarWidget()
        self.strasseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Save")

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit) #String = Labelname
        layout.addRow("Name:", self.nameLineEdit) #String = Labelname
        layout.addRow("Email:", self.emailLineEdit)
        layout.addRow("Geburtstag:", self.ageCalendarWidget)
        layout.addRow("Strasse:", self.strasseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.countries)
        layout.addRow(self.button)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.menu_save)
        

    def menu_save(self):
        file = open("Addresse.csv", "w", encoding= "utf-8")
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        email = self.emailLineEdit.text()
        geb = self.ageCalendarWidget.selectedDate().toString("yyyy-MM-dd")
        strasse = self.strasseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.countries.currentText() 
        file.write(f"{vorname},{name},{email},{geb},{strasse},{plz},{ort},{land}")
        

        #print("Menu Save wurde gewählt...")
        file.close()

    def menu_quit(self):
        #print("Menu Quit wurde gewählt...")
        self.close()  # Hauptfenster schliessen = beenden!


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()





