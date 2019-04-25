from PyQt5 import QtGui
from PyQt5.QtWidgets import  QWidget, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
import random
from End import End
from Hex import Hex
from Map import Map


class Game(QMainWindow):
    def __init__(self, app = None):
        super(Game, self).__init__(app)

        self.title = "2048 HEX"
        self.app = app
        self.hex = [Hex(-40,-170,0, self), Hex(-110,-130,0, self), Hex(30,-130,0, self), Hex(-40,-90,0, self), Hex(-110,-50,0, self), Hex(30,-50,0, self), Hex(-40,-10,0, self)]
        self.point = [[0, self.hex[0], 0], [self.hex[1], 0, self.hex[2]], [0, self.hex[3], 0], [self.hex[4], 0, self.hex[5]], [0, self.hex[6], 0]]
        self.end = End(self.app, self)

        self.height = 480
        self.width = 640

        self.scene = QGraphicsScene(-self.width/2, -self.height/2, self.width, self.height)
        self.view = QGraphicsView()

        self.column = len(self.point[0])
        self.rows = len(self.point)
        self.lose = False
        self.window = QWidget()

        self.initUI()
        self.setTimer()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.view.setRenderHints(QtGui.QPainter.Antialiasing |
           QtGui.QPainter.HighQualityAntialiasing)

        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
        self.scene.setBackgroundBrush(QColor(0, 100, 255))

        self.draw()

    def draw(self):
        self.scene.addItem(Map(-40,0,self))
        self.scene.addItem(self.hex[0])
        self.scene.addItem(self.hex[1])
        self.scene.addItem(self.hex[2])
        self.scene.addItem(self.hex[3])
        self.scene.addItem(self.hex[4])
        self.scene.addItem(self.hex[5])
        self.scene.addItem(self.hex[6])

    def up(self):

        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        while True:
                            counter = counter + 2
                            if r - counter >= 0:
                                if self.point[r - counter][c].value == 0:
                                    self.point[r - counter][c].value = self.point[_r][c].value
                                    self.point[_r][c].value = 0
                                    _r = _r - counter
                                elif self.point[r - counter][c].value == self.point[_r][c].value:
                                    self.point[r - counter][c].value = self.point[_r][c].value + self.point[r - counter][c].value
                                    self.point[_r][c].value = 0

                            if r - counter <= 0:
                                break
        self.random()


    def upRight(self):
        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        _c = c
                        while True:
                            counter = counter + 1
                            if c + counter < self.column and r - counter >= 0:
                                if self.point[r - counter][c + counter].value == 0:
                                    self.point[r - counter][c + counter].value = self.point[_r][_c].value
                                    self.point[_r][_c].value = 0
                                    _r = _r - counter
                                    _c = _c + counter
                                elif self.point[r - counter][c + counter].value == self.point[_r][_c].value:
                                    self.point[r - counter][c + counter].value = self.point[_r][_c].value + \
                                                                                 self.point[r - counter][
                                                                                     c + counter].value
                                    self.point[_r][_c].value = 0

                            if c + counter >= self.column and r - counter <= 0:
                                break
        self.random()

    def upLeft(self):
        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        _c = c
                        while True:
                            counter = counter + 1
                            if c - counter >= 0 and r - counter >= 0:
                                if self.point[r - counter][c - counter].value == 0:
                                    self.point[r - counter][c - counter].value = self.point[_r][_c].value
                                    self.point[_r][_c].value = 0
                                    _r = _r - counter
                                    _c = _c - counter
                                elif self.point[r - counter][c - counter].value == self.point[_r][_c].value:
                                    self.point[r - counter][c - counter].value = self.point[_r][_c].value + self.point[r - counter][c - counter].value
                                    self.point[_r][_c].value = 0

                            if c - counter <= 0 and r - counter <= 0:
                                break
        self.random()

    def down(self):
        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        while True:
                            counter = counter + 2
                            if r + counter < self.rows:
                                if self.point[r + counter][c].value == 0:
                                    self.point[r + counter][c].value = self.point[_r][c].value
                                    self.point[_r][c].value = 0
                                    _r = _r + counter
                                elif self.point[r + counter][c].value == self.point[_r][c].value:
                                    self.point[r + counter][c].value = self.point[_r][c].value + self.point[r + counter][c].value
                                    self.point[_r][c].value = 0

                            if r + counter >= self.rows:
                                break
        self.random()

    def downRight(self):
        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        _c = c
                        while True:
                            counter = counter + 1
                            if c + counter < self.column and r + counter < self.rows:
                                if self.point[r + counter][c + counter].value == 0:
                                    self.point[r + counter][c + counter].value = self.point[_r][_c].value
                                    self.point[_r][_c].value = 0
                                    _r = _r + counter
                                    _c = _c + counter
                                elif self.point[r + counter][c + counter].value == self.point[_r][_c].value:
                                    self.point[r + counter][c + counter].value = self.point[_r][_c].value + \
                                                                                 self.point[r + counter][
                                                                                     c + counter].value
                                    self.point[_r][_c].value = 0

                            if c + counter >= self.column and r + counter >= self.rows:
                                break
        self.random()


    def downLeft(self):
        for r in range(self.rows):
            for c in range(self.column):
                if type(self.point[r][c]) is Hex:
                    if self.point[r][c].value > 0:
                        counter = 0
                        _r = r
                        _c = c
                        while True:
                            counter = counter + 1
                            if c - counter >= 0 and r + counter < self.rows:
                                if self.point[r + counter][c - counter].value == 0:
                                    self.point[r + counter][c - counter].value = self.point[_r][_c].value
                                    self.point[_r][_c].value = 0
                                    _r = _r - counter
                                    _c = _c - counter
                                elif self.point[r + counter][c - counter].value == self.point[_r][_c].value:
                                    self.point[r + counter][c - counter].value = self.point[_r][_c].value + self.point[r + counter][c - counter].value
                                    self.point[_r][_c].value = 0

                            if c - counter <= 0 and r + counter >= self.rows:
                                break
        self.random()

    def getScore(self):
        values = []
        for val in self.hex:
            values.append(val.value)
        return str(max(values))

    def setTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(100)

    def timerEvent(self):
        self.visibility()
        for _hex in self.hex:
            if _hex.up is True:
                self.up()
                _hex.up = False
            elif _hex.upLeft is True:
                self.upLeft()
                _hex.upLeft = False
            elif _hex.upRight is True:
                self.upRight()
                _hex.upRight = False
            elif _hex.down is True:
                self.down()
                _hex.down = False
            elif _hex.downLeft is True:
                self.downLeft()
                _hex.downLeft = False
            elif _hex.downRight is True:
                self.downRight()
                _hex.downRight = False

        self.checkIfLose()

    def visibility(self):
        for _hex in self.hex:
            if _hex.value == 0:
                _hex.setVisible(False)
            else: _hex.setVisible(True)

    def refresh(self):
        for row in range(5):
            for column in range(3):
                if type(self.point[row][column]) is Hex:
                    self.point[row][column].refresh()

    def random(self):
        self.checkIfLose()
        if self.lose == False:
            while True:
                randomValue = random.randrange(0, 7)
                if self.hex[randomValue].value == 0:
                    break
            self.hex[randomValue].value = 2

    def checkIfLose(self):
        cnt = 0
        for i in range(len(self.hex)):
           if self.hex[i].value != 0:
               cnt = cnt + 1

        if cnt == 7:
            self.lose = True
            self.end.label.setText("Wynik: " + self.getScore())
            self.app.setScore(self.getScore())
            self.end.show()

    def start(self):
        self.random()
        self.random()

    def clear(self):
        self.lose = False
        for h in self.hex:
            h.value = 0
        self.app.setScore(0)
        self.start()
