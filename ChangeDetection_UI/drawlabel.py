# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class MyLabel(QLabel):
    # 鼠标点击事件
    def __init__(self):
        super(MyLabel, self).__init__()
        self.start_point = QPoint(-1, -1)
        self.end_point = QPoint(-1, -1)
        img = QPixmap('img/label.png')
        # img = img.scaled(self.width(), self.height())
        img = img.scaled(300, 300)
        self.setPixmap(img)
        self.penwidth = 3
        self.color = Qt.white

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = self.start_point

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end_point = event.pos()
            self.update()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.end_point = event.pos()
            self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.pixmap())
        painter.setPen(QPen(self.color, self.penwidth, Qt.SolidLine))
        painter.drawLine(self.start_point, self.end_point)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap())  # .scaled(self.width(), self.height())
        self.setScaledContents(True)

        self.start_point = self.end_point


