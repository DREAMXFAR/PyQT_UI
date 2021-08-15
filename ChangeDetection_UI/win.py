# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class DrawWindow(QDialog):
    def __init__(self):
        super(DrawWindow, self).__init__()
        # 设置主窗口布局
        self.setUIGeometry()

    def setUIGeometry(self):
        """
        设置主窗口居中布局，尺寸大小
        """
        # 设置标题
        self.setWindowTitle('基于变化检测的自然资源检测综合系统')
        # 设置尺寸
        width = 1000
        height = 500
        self.resize(width, height)
        size = self.geometry()
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 移动窗口
        x = int((screen.width()-size.width())/2)
        y = int((screen.height()-size.height()-100)/2)
        self.move(x, y)

    def initUI(self):
        pass

    def mousePressEvent(self, event):
        # 鼠标左键按下
        print('鼠标按下')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/icon.png'))
    window = DrawWindow()
    window.show()

    sys.exit(app.exec_())
