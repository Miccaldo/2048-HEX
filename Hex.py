from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPolygonF, QPen, QFont, QBrush
from PyQt5.QtCore import Qt, QRectF, QPointF
import pyautogui

class Hex(QGraphicsItem):
    def __init__(self, x, y, value, parent=None):
        super(Hex, self).__init__()

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        self.x = x
        self.y = y
        self.size = 75
        self.gesturesX = []
        self.gesturesY = []

        self.startX = 0
        self.startY = 0
        self.startFlag = False

        self.moveX = 0
        self.moveY = 0

        self.value = value
        self.setAcceptHoverEvents(True)

        self.up = False
        self.down = False
        self.upLeft = False
        self.upRight = False
        self.downLeft = False
        self.downRight = False

        self.cntX = x
        self.cntY = y

        self.newIndexColumn = 0
        self.newIndexRow = 5
        self.valueBuf = self.value
        self.paintFlag = True
        self.pen = QPen(Qt.black)
        self.pen.setWidth(5)

        self.brush = QBrush(QtCore.Qt.blue)
        self.parent = parent

        self.toleranceX = 20
        self.toleranceY = 20
        self.verticalRange = 50
        self.horizontalRange = 100

        self.rect = QtCore.QRectF(self.x, self.y, self.size, self.size)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget=None):
            painter.setBrush(self.brush)
            painter.setPen(self.pen)
            painter.drawPolygon(QPolygonF([QPointF(self.x + 60, self.y + 5), QPointF(self.x + 75, self.y + 40), QPointF(self.x + 60, self.y + 70),
                                      QPointF(self.x + 15, self.y + 70), QPointF(self.x + 0, self.y + 40), QPointF(self.x + 15, self.y + 5)]))
            self.drawText(painter)

    def drawText(self, painter):
        brush = QBrush(Qt.black)
        pencil = QPen()
        pencil.setColor(Qt.black)
        pencil.setBrush(brush)
        painter.setPen(pencil)
        font = QFont("Impact", 16)

        painter.setFont(font)
        painter.drawText(QRectF(self.x - 62, self.y + 17, 200, 40), Qt.AlignCenter, str(self.value))

    def mouseMoveEvent(self, event):
        self.saveCoordinates()
        QGraphicsItem.mouseMoveEvent(self, event)

    def saveCoordinates(self):
        self.moveX, self.moveY = pyautogui.position()
        valX = self.startX - self.moveX
        valY = self.startY - self.moveY

        self.gesturesX.append(valX)
        self.gesturesY.append(valY)

    def mousePressEvent(self, event):
        self.startX, self.startY = pyautogui.position()
        QGraphicsItem.mousePressEvent(self, event)

    def hoverEnterEvent(self, event):
        self.pen.setColor(Qt.green)
        QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.pen.setStyle(QtCore.Qt.SolidLine)
        self.pen.setColor(Qt.black)

        QGraphicsItem.hoverLeaveEvent(self, event)

    def mouseReleaseEvent(self, event):

        self.checkDir()

        self.setX(0)
        self.setY(0)
        QGraphicsItem.mouseReleaseEvent(self, event)

    def checkDir(self):
        self.moveX, self.moveY = pyautogui.position()

        gesturesXBuf = []
        gesturesYBuf = []

        upLeft = Flags()
        upRight = Flags()
        downLeft = Flags()
        downRight = Flags()

        verticalBuf = 0

        length = len(self.gesturesX)

# *********************** UP LEFT ***************************       #   GESTURE:
                                                                    # <---
        for x in range(length):                                     #     |
            gesturesXBuf.append(self.gesturesX[x])                  #     |
            gesturesYBuf.append((self.gesturesY[x]))
            left = max(gesturesXBuf)
            right = abs(min(gesturesXBuf))
            down = abs(min(gesturesYBuf))
            up = max(gesturesYBuf)

            if upLeft.flag is False:
                if left > self.toleranceX or up < self.verticalRange:
                    upLeft.flag = False
                else:
                    upLeft.flag = True

            if upLeft.flag is True:
                if upLeft.flag2 is False:
                    if left > self.toleranceX:
                        verticalBuf = up
                        gesturesXBuf.clear()
                        gesturesYBuf.clear()
                        upLeft.flag2 = True
                if upLeft.flag2 is True:
                    if up - verticalBuf > self.toleranceY or verticalBuf - down > self.toleranceY or left < self.horizontalRange:
                        upLeft.flag3 = False
                    else:
                        upLeft.flag3 = True

# *********************** UP RIGHT ***************************

            if upRight.flag is False:                                       #   GESTURE:
                if right > self.toleranceX or up < self.verticalRange:      #    --->
                    upRight.flag = False                                    #   |
                else:                                                       #   |
                    upRight.flag = True

            if upRight.flag is True:
                if upRight.flag2 is False:
                    if right > self.toleranceX:
                        verticalBuf = up
                        gesturesXBuf.clear()
                        gesturesYBuf.clear()
                        upRight.flag2 = True
                if upRight.flag2 is True:
                    if up - verticalBuf > self.toleranceY or verticalBuf - down > self.toleranceY or right < self.horizontalRange:
                        upRight.flag3 = False
                    else:
                        upRight.flag3 = True

# *********************** DOWN RIGHT ***************************

            if downRight.flag is False:                                        #     GESTURE:
                if right > self.toleranceX or down < self.verticalRange:       #     |
                    downRight.flag = False                                     #     |
                else:                                                          # <---
                    downRight.flag = True

            if downRight.flag is True:
                if downRight.flag2 is False:
                    if right > self.toleranceX:
                        verticalBuf = down
                        gesturesXBuf.clear()
                        gesturesYBuf.clear()
                        downRight.flag2 = True
                if downRight.flag2 is True:
                    if down - verticalBuf > self.toleranceY or verticalBuf - abs(up) > self.toleranceY or right < self.horizontalRange:
                        downRight.flag3 = False
                    else:
                        downRight.flag3 = True

# *********************** DOWN LEFT ***************************

            if downLeft.flag is False:                                      #      GESTURE:
                if left > self.toleranceX or down < self.verticalRange:     #   |
                    downLeft.flag = False                                   #   |
                else:                                                       #    --->
                    downLeft.flag = True

            if downLeft.flag is True:
                if downLeft.flag2 is False:
                    if left > self.toleranceX:
                        verticalBuf = down
                        gesturesXBuf.clear()
                        gesturesYBuf.clear()
                        downLeft.flag2 = True
                if downLeft.flag2 is True:
                    if down - verticalBuf > self.toleranceY or verticalBuf - abs(
                            up) > self.toleranceY or left < self.horizontalRange:
                        downLeft.flag3 = False
                    else:
                        downLeft.flag3 = True

        if upRight.flag is True and upRight.flag2 is False and upRight.flag3 is False: self.up = True
        elif downRight.flag is True and downRight.flag2 is False and downRight.flag3 is False: self.down = True
        elif upRight.flag3 is True: self.upRight = True
        elif upLeft.flag3 is True: self.upLeft = True
        elif downRight.flag3 is True: self.downRight = True
        elif downLeft.flag3 is True: self.downLeft = True

        self.gesturesX.clear()
        self.gesturesY.clear()

        self.gesturesX.append(0)
        self.gesturesY.append(0)


class Flags:
    def __init__(self):
        self.flag = False
        self.flag2 = False
        self.flag3 = False
