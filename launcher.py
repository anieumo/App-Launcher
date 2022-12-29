import sys
import os
import shutil

from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCompleter, QComboBox

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.imovie = QPushButton("iMovie")
        self.imovie.clicked.connect(self.launchimovie)
        self.photobooth = QPushButton("Photo Booth")
        self.photobooth.clicked.connect(self.launchphotobooth)
        self.music = QPushButton("Music")
        self.music.clicked.connect(self.launchmusic)
        self.calculator = QPushButton("Calculator")
        self.calculator.clicked.connect(self.launchcalculator)
        self.obs = QPushButton("OBS")
        self.obs.clicked.connect(self.launchobs)
        self.garageband = QPushButton("Garageband")
        self.garageband.clicked.connect(self.launchgarageband)
        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.update)
        self.combobox = QComboBox()
        self.combobox.setGeometry(QRect(30, 30, 10, 30))
        self.combobox.addItem("All")
        self.combobox.addItem("Music")
        self.combobox.addItem("Video")
        self.combobox.currentIndexChanged.connect(self.setmode)

        
        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.searchbar)

        self.list = [self.imovie, self.photobooth, self.music, self.calculator, self.obs,
            self.garageband]
        self.newlist = []

        for item in self.list:
            self.layout.addWidget(item)
        


        self.setCentralWidget(self.container)

    def hide(self):
        self.imovie.hide()
        self.photobooth.hide()
        self.music.hide()
        self.calculator.hide()
        self.obs.hide()
        self.garageband.hide()
    
    def setmode(self):
        self.hide()
        print(self.combobox.currentIndexChanged)
        if self.combobox.currentIndex() == 0:
            self.imovie.show()
            self.photobooth.show()
            self.music.show()
            self.calculator.show()
            self.obs.show()
            self.garageband.show()
        if self.combobox.currentIndex() == 1:
            self.imovie.show()
            self.music.show()
            self.garageband.show()
        else:
            self.photobooth.show()
            self.imovie.show()
            self.obs.show()

    def update(self, text):
        self.hide()
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()
            if isinstance(item, QPushButton):
                if self.searchbar.text().lower() in item.text().lower():
                    item.show()
                    print(item.text())
        print(self.searchbar.text())


    def launchimovie(self):
        os.system("open /Applications/iMovie.app")

    def launchphotobooth(self):
        os.system("open /System/Applications/Photo\ Booth.app")

    def launchmusic(self):
        os.system("open /System/Applications/Music.app")

    def launchcalculator(self):
        os.system("open /System/Applications/Calculator.app")

    def launchobs(self):
        os.system("open /Applications/OBS.app")

    def launchgarageband(self):
        os.system("open /Applications/GarageBand.app")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()