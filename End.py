from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QFont


class End(QWidget):
    def __init__(self, app, game):
        super().__init__()

        self.app = app
        self.game = game
        self.setWindowTitle("Wyniki")
        self.button = QPushButton(self)
        self.label = QLabel(self)
        self.width = 200
        self.height = 150

        self.InitLayout()
        self.Init()
        self.InitControls()

    def Init(self):
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setMaximumHeight(self.height)
        self.setMaximumWidth(self.width)
        self.setfButton()
        self.setfLabel()
        self.setColor()
    def InitControls(self):
        self.button.setText("Dalej")
        self.button.clicked.connect(self.end_Clicked)
    def InitLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def setfButton(self):
        myFont = QFont()
        myFont.setBold(True)
        self.button.setFont(QFont("Impact", 10))
    def setfLabel(self):
        myFont = QFont()
        myFont.setBold(True)
        self.label.setFont(QFont("Impact", 18, weight=QtGui.QFont.Bold))
    def setColor(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QtGui.QColor(100, 100, 255))
        self.setPalette(palette)
    def end_Clicked(self):
        self.close()
        self.app.saveScore()
        self.game.clear()
        self.game.close()
        self.app.show()