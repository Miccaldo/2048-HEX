from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget
from PyQt5.QtGui import QPalette, QFont

class ScoreList(QWidget):
    def __init__(self, app):
        super().__init__()

        self.list = QListWidget()
        self.app = app
        self.width = 300
        self.height = 400
        self.label = QLabel()
        self.button = QPushButton()

        self.refresh()

        self.Init()

    def Init(self):
        self.setMaximumHeight(self.height)
        self.setMaximumWidth(self.width)
        self.InitControls()
        self.InitLayout()
        self.setColor()
        self.setf()
        self.setfLabel()
        self.setfButton()

    def InitControls(self):
        self.label.setText("Wyniki")
        self.button.setText("Dalej")
        self.button.clicked.connect(self.next_Click)
    def InitLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def setColor(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QtGui.QColor(100, 100, 255))
        self.setPalette(palette)
    def setf(self):
        myFont = QFont()
        myFont.setBold(True)
        self.setFont(QFont("Impact", 10))
    def setfButton(self):
        myFont = QFont()
        myFont.setBold(True)
        self.button.setFont(QFont("Impact", 14))
    def setfLabel(self):
        myFont = QFont()
        myFont.setBold(True)
        self.label.setFont(QFont("Impact", 14))
    def next_Click(self):
        self.close()
    def getLinesFromFile(self):
        file = open(self.app.getScoreFilePath(), 'r')
        lines = file.read().splitlines()
        file.close()
        return lines
    def getScoreNumber(self):
        return len(self.scores)

    def refresh(self):
        self.list.clear()

        self.list.addItems(self.sort())
        self.app.setScoreNumber(self.getScoreNumber())

    def sort(self):
        self.scores = self.getLinesFromFile()
        bufor = []
        split = []
        sort = []
        max = 0
        index = 0

        for i in range(len(self.scores)):
            bufor.append(self.scores[i].split())
            split.append(int(bufor[i][2]))

        for i in range(len(split)):
            for j in range(len(split)):

                if split[j] > max:
                    max = split[j]
                    index = j

            max = 0
            split[index] = 0
            sort.append("{}. Gracz: ".format(i + 1) + bufor[index][2])
        return sort
