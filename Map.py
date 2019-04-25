from PyQt5 import  QtCore
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF

class Map(QGraphicsItem):
    def __init__(self, x, y, parent=None):
        super(Map, self).__init__()

        self.x = x
        self.y = y
        self.size = 75

        self.pen = QPen(Qt.black)
        self.pen.setWidth(5)

        self.brush = QBrush(QColor(50, 80, 255))
        self.parent = parent
        self.polygon = QPolygonF([QPointF(self.x + 70, self.y - 180),QPointF(self.x + 90, self.y - 140),QPointF(self.x + 140, self.y - 140),
                                  QPointF(self.x + 160, self.y - 90), QPointF(self.x + 143, self.y - 50),
                                  QPointF(self.x + 160, self.y - 10), QPointF(self.x + 140, self.y + 35),
                                  QPointF(self.x + 90, self.y + 35), QPointF(self.x + 70, self.y + 75),
                                  QPointF(self.x + 5, self.y + 75), QPointF(self.x - 15, self.y + 35),
                                  QPointF(self.x - 65, self.y + 35), QPointF(self.x - 85, self.y - 10),
                                  QPointF(self.x - 68, self.y - 50), QPointF(self.x - 85, self.y - 90),
                                  QPointF(self.x - 85, self.y - 90), QPointF(self.x - 65, self.y - 140),
                                  QPointF(self.x - 15, self.y - 140), QPointF(self.x + 5, self.y - 180)])

        self.rect = QtCore.QRectF(self.x, self.y, self.size, self.size)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget=None):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawPolygon(self.polygon)


