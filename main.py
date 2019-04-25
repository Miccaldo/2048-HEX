from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette, QFont
from tkinter import *
from Game import Game
from ScoreList import ScoreList
from Button import Button

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = '2048 HEX'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.score = 0
        self.scoreNumber = 0

        self.newGame = Button("nowa gra")
        self.scores = Button("Wyniki")
        self.end = Button(" ")

        self.scoreFile = "scores.txt"
        self.scoreList = ScoreList(self)

        self.initUI()
        self.layout()
        self.addHandles()

        self.game = Game(self)

    def getScoreFilePath(self):
        return self.scoreFile

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.end.setIcon(QtGui.QIcon('images/exit.png'))
        self.end.setIconSize(QtCore.QSize(50, 50))
        self.setColor()
        self.setf()
        self.show()

    def layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.newGame)
        layout.addWidget(self.scores)
        layout.addWidget(self.end)
        self.setLayout(layout)

    def addHandles(self):
        self.newGame.clicked.connect(self.newGame_Click)
        self.scores.clicked.connect(self.scores_Click)
        self.end.clicked.connect(app.exit)

    def newGame_Click(self):
        self.close()
        self.game.show()
        self.game.start()
    def setColor(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QtGui.QColor(0, 100, 255))
        self.setPalette(palette)

    def setf(self):
        myFont = QFont()
        myFont.setBold(True)
        self.setFont(QFont("Impact", 10))

    def scores_Click(self):
        self.scoreList.refresh()
        self.scoreList.show()

    def saveScore(self):
        file = open(self.scoreFile, 'a')
        self.scoreNumber = self.scoreNumber + 1
        line_p1 = "{}".format(self.scoreNumber)
        line_p2 = ". Gracz: "
        line_p3 = str(self.score)
        line_p4 = "\n"

        file.write(line_p1 + line_p2 + line_p3 + line_p4)
        file.close()
    def setScore(self, score):
        self.score = score
    def getScore(self):
        return self.score
    def setScoreNumber(self, scoreNumber):
        self.scoreNumber = scoreNumber
    def getScoreNumber(self):
        return self.scoreNumber


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
