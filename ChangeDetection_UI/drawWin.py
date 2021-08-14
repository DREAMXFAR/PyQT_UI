# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class DrawWindow(object):
    def __init__(self, dialog, imageAfter_path=None, imageBefore_path=None, changeResult_path=None):
        super(DrawWindow, self).__init__()
        self.dialog = dialog
        self.imageAfter_path = imageAfter_path
        self.imageBefore_path = imageBefore_path
        self.changeResult_path = changeResult_path
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
        width = 1000
        height = 500
        self.dialog.resize(width, height)
        size = self.dialog.geometry()
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 移动窗口
        x = int((screen.width()-size.width())/2)
        y = int((screen.height()-size.height()-100)/2)
        self.dialog.move(x, y)

    def initUI(self):
        cd_layout = QGridLayout(self.dialog)

        drawBtns = self.drawBtns()
        cd_layout.addWidget(drawBtns, 1, 1, 1, 3)

        # image
        image_res = self.imageShow()
        cd_layout.addWidget(image_res, 2, 1, 3, 3)

        self.dialog.setLayout(cd_layout)

    def drawBtns(self):
        # 用于接收布局的对象
        hbox = QGroupBox('调整选项')
        # 设置布局
        drawBtnslayout = QHBoxLayout(hbox)
        # 导入文件夹导入
        Btn5 = QPushButton('画笔粗细', hbox)
        drawBtnslayout.addWidget(Btn5, alignment=Qt.AlignCenter)
        # 导入文件夹导入
        Btn6 = QPushButton('颜色选项', hbox)
        drawBtnslayout.addWidget(Btn6, alignment=Qt.AlignCenter)
        # 导入文件夹导入
        Btn1 = QPushButton('绘制', hbox)
        drawBtnslayout.addWidget(Btn1, alignment=Qt.AlignCenter)
        # 选择图像导入
        Btn2 = QPushButton('擦除', hbox)
        drawBtnslayout.addWidget(Btn2, alignment=Qt.AlignCenter)
        # 检测按钮
        Btn3 = QPushButton('确定', hbox)
        drawBtnslayout.addWidget(Btn3, alignment=Qt.AlignCenter)
        Btn3.clicked.connect(self.dialog.close)
        # 退出按钮
        Btn4 = QPushButton('退出', hbox)
        drawBtnslayout.addWidget(Btn4, alignment=Qt.AlignCenter)
        Btn4.clicked.connect(self.dialog.close)
        # 添加布局
        hbox.setLayout(drawBtnslayout)
        # 返回布局对象
        return hbox

    def imageShow(self):
        # 用于接收布局的对象
        hbox = QWidget()
        # 设置布局
        imageslayout = QHBoxLayout(hbox)
        # 时相一
        imgbefore_res = QLabel(self.dialog)
        if self.imageBefore_path is None:
            self.imageBefore_path = r'img/before.png'
        imgbefore_res.setPixmap(QPixmap(self.imageBefore_path))
        imgbefore_res.setScaledContents(True)
        imageslayout.addWidget(imgbefore_res)
        # 时相二
        imgafter_res = QLabel(self.dialog)
        if self.imageAfter_path is None:
            self.imageAfter_path = r'img/after.png'
        imgafter_res.setPixmap(QPixmap(self.imageAfter_path))
        imgafter_res.setScaledContents(True)
        imageslayout.addWidget(imgafter_res)

        # 监测结果
        cd_res = QLabel(self.dialog)
        # cd_res.setPixmap(QPixmap(r'img/label.png'))
        print(self.imageAfter_path)
        if self.changeResult_path is None:
            self.changeResult_path = r'img/label.png'
        cd_res.setPixmap(QPixmap(self.changeResult_path))
        cd_res.setScaledContents(True)
        imageslayout.addWidget(cd_res)

        # 添加布局
        hbox.setLayout(imageslayout)
        # 返回布局对象
        return hbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/icon.png'))
    window = DrawWindow(QDialog(), 'img/icon.png')
    window.dialog.show()

    sys.exit(app.exec_())


