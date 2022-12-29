import sys
import os
import shutil

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCompleter

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
        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.update)
        
        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)
        self.layout.addWidget(self.searchbar)

        self.list = [self.imovie, self.photobooth, self.music, self.calculator, self.obs]
        self.newlist = []

        for item in self.list:
            self.layout.addWidget(item)


        self.setCentralWidget(self.container)
    
    def clearLayout(self):
        self.layout.removeWidget(self.imoviebutton)
        self.layout.removeWidget(self.photoboothbutton)
        self.layout.removeWidget(self.musicbutton)

    def hide(self):
        self.imovie.hide()
        self.photobooth.hide()
        self.music.hide()
        self.calculator.hide()
        self.obs.hide()

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



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()