# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class DrawWindow(object):
    def __init__(self, dialog):
        super(DrawWindow, self).__init__()
        self.dialog = dialog
        # self.changemap = changemap
        self.setUIGeometry()  # 设置主窗口布局
        self.initUI()

    def setUIGeometry(self):
        """
        设置主窗口居中布局，尺寸大小
        """
        # 设置标题
        self.dialog.setWindowTitle('基于变化检测的自然资源检测综合系统')
        # 设置尺寸
        width = 500
        height = 400
        self.dialog.resize(width, height)
        size = self.dialog.geometry()
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 移动窗口
        x = int((screen.width()-size.width())/2)
        y = int((screen.height()-size.height()-100)/2)
        self.dialog.move(x, y)

    def initUI(self):
        cd_layout = QVBoxLayout(self.dialog)

        cd_res = QLabel(self.dialog)
        cd_res.setPixmap(QPixmap(r'img/label.png'))
        cd_res.setScaledContents(True)
        cd_layout.addWidget(cd_res)

        self.dialog.setLayout(cd_layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/icon.png'))
    window = DrawWindow(QDialog())
    window.dialog.show()

    sys.exit(app.exec_())


