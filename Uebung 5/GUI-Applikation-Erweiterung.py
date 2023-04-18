import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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

        #Menu-Bar erstellen (File)
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        filemenu.addAction(save)
        filemenu.addSeparator()
        save.triggered.connect(self.menu_save)
        load = QAction("Load...", self)
        filemenu.addAction(load)
        filemenu.addSeparator()
        load.triggered.connect(self.load)
        quit = QAction("Quit", self)
        filemenu.addAction(quit)
        quit.triggered.connect(self.menu_quit)

        #Menu-Bar erstellen (View)
        menubar2 = self.menuBar()
        viewmenu = menubar2.addMenu("View")
        view = QAction("View on Map", self)
        viewmenu.addAction(view)
        view.triggered.connect(self.karte)
        
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
        buttonload = QPushButton("Lade..")
        buttonsave = QPushButton("Auf Karte anzeigen")

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
        layout.addWidget(buttonload)
        layout.addWidget(buttonsave)
        layout.addRow(self.button)

        buttonload.clicked.connect(self.load)
        buttonsave.clicked.connect(self.karte)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.menu_save)

    def karte(self):
        link = f"https://www.google.ch/maps/place/{self.strasse.text()}+{self.ort.text()}+{self.countries.currentText()}"
        QDesktopServices.openUrl(QUrl(link))

    def load(self):
        #documents = QStandardPaths.standardLocations QStandardPaths.Doc <---falsch
        #QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Python Files (*.py)")
        #QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Files (*.txt)")
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Files (*.txt);;Python Files (*.py)")
        #filename, filter = QFileDialog.getOpenFileNames(self, "Datei öffnen", "", "Text Files (*.txt);;Python Files (*.py)") <--mehrere aufrufen

        if filename != "":
            with open(filename, "r", encoding= "utf-8") as file:
                for data in file:
                    daten = data.strip()
                    QMessageBox.about(self, f"Daten von {filename}", daten)
            #print(filename)
            #print(filter)

        else:
            QMessageBox.warning(self, "Warning", "No File chosen")
            
    def menu_save(self):
        filename,filter = QFileDialog.getSaveFileName(self, "Datei speichern","","Text Datei(*.txt)")
        if filename != "":
            file = open(filename, "w", encoding= "utf-8")
            vorname = self.vorname.text()
            name = self.name.text()
            email = self.email.text()
            geb = self.age.selectedDate().toString("dd.MM.yyyy")
            strasse = self.strasse.text()
            plz = self.plz.text()
            ort = self.ort.text()
            land = self.countries.currentText() 
            file.write(f"{vorname},{name},{email},{geb},{strasse},{plz},{ort},{land}")
            print(filename, filter)
            #print("Menu Save wurde gewählt...")
            file.close()

        else:
            QMessageBox.warning(self, "Warning", "File already exits!!!")

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





