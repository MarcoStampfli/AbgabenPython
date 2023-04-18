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

        #Menu-Bar erstellen (file)
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        filemenu.addAction(save)
        filemenu.addSeparator()
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        filemenu.addAction(quit)
        quit.triggered.connect(self.menu_quit)

        #Menu-Bar erstellen (View)
        menubar2 = self.menuBar()
        viewmenu = menubar2.addMenu("View")
        view = QAction("View on Map", self)
        viewmenu.addAction(view)
        #view.triggered.connect(self.karte)
        
        # Widget-Instanzen erstellen:

        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.email = QLineEdit()
        self.age = QCalendarWidget()
        #self.age = QDateEdit()
        self.strasse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Save")

        # Layout füllen:
        layout.addRow("Vorname:", self.vorname) #String = Labelname
        layout.addRow("Name:", self.name) #String = Labelname
        layout.addRow("Email:", self.email)
        layout.addRow("Geburtstag:", self.age)
        #layout.addrow("Geburtstag:", self.age)
        layout.addRow("Strasse:", self.strasse)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
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
        vorname = self.vorname.text()
        name = self.name.text()
        email = self.email.text()
        geb = self.age.selectedDate().toString("dd.MM.yyyy")
        strasse = self.strasse.text()
        plz = self.plz.text()
        ort = self.ort.text()
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





