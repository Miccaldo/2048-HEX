import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QGridLayout, QListView, QListWidget
from PyQt5.QtGui import QPalette, QPolygonF, QPainter, QPen, QPolygon, QColor, QPixmap, QFont, QIcon
from PyQt5.QtCore import QPoint, Qt, QTimer


class Button(QPushButton):
    def __init__(self, name):
        QPushButton.__init__(self)

        self.button = QPushButton()
        self.name = name
        self.height = 80
        self.init()

    def init(self):
        self.setText(str(self.name))
        self.setMinimumHeight(self.height)
