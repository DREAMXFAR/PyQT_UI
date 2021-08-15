# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from drawlabel import MyLabel


class DrawWindow(QDialog):
    def __init__(self, imageAfter_path=None, imageBefore_path=None, changeResult_path=None):
        super(DrawWindow, self).__init__()
        # images
        self.imageAfter_path = imageAfter_path
        self.imageBefore_path = imageBefore_path
        self.changeResult_path = changeResult_path
        # self.changemap = changemap
        # 设置主窗口布局
        self.setUIGeometry()
        self.initUI()
        # 绘图函数
        self.lastPoint = QPoint()  # 起始点
        self.endPoint = QPoint()  # 终点
        self.penwidth = 3

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
        x = int((screen.width() - size.width()) / 2)
        y = int((screen.height() - size.height() - 100) / 2)
        self.move(x, y)

    def initUI(self):
        cd_layout = QGridLayout(self)
        # buttons
        drawBtns = self.drawBtns()
        cd_layout.addWidget(drawBtns, 1, 1, 1, 3)
        # image
        image_res = self.imageShow()
        cd_layout.addWidget(image_res, 2, 1, 3, 3)
        self.setLayout(cd_layout)

    def drawBtns(self):
        # 用于接收布局的对象
        hbox = QGroupBox('调整选项')
        # 设置布局
        drawBtnslayout = QHBoxLayout(hbox)
        # 导入文件夹导入
        Btn5 = QPushButton('画笔粗细', hbox)
        drawBtnslayout.addWidget(Btn5, alignment=Qt.AlignCenter)
        Btn5.clicked.connect(self.setPenwidth)
        # 导入文件夹导入
        Btn6 = QPushButton('颜色选项', hbox)
        drawBtnslayout.addWidget(Btn6, alignment=Qt.AlignCenter)
        Btn6.clicked.connect(self.getColor)
        # 导入文件夹导入
        Btn1 = QPushButton('绘制', hbox)
        drawBtnslayout.addWidget(Btn1, alignment=Qt.AlignCenter)
        Btn1.clicked.connect(self.draw)
        # 选择图像导入
        Btn2 = QPushButton('擦除', hbox)
        drawBtnslayout.addWidget(Btn2, alignment=Qt.AlignCenter)
        Btn2.clicked.connect(self.erase)
        # 检测按钮
        Btn3 = QPushButton('确定', hbox)
        drawBtnslayout.addWidget(Btn3, alignment=Qt.AlignCenter)
        Btn3.clicked.connect(self.close)
        # 退出按钮
        Btn4 = QPushButton('退出', hbox)
        drawBtnslayout.addWidget(Btn4, alignment=Qt.AlignCenter)
        Btn4.clicked.connect(self.close)
        # 添加布局
        hbox.setLayout(drawBtnslayout)
        # 返回布局对象
        return hbox

    def imageShow(self):
        # 用于接收布局的对象
        hbox = QWidget(self)
        # 设置布局
        imageslayout = QGridLayout(hbox)
        # 时相一
        groupbox1 = QGroupBox('参考图像: 时相一', hbox)
        layout1 = QHBoxLayout(groupbox1)
        imgbefore_res = QLabel(self)
        if self.imageBefore_path is None:
            self.imageBefore_path = r'img/before.png'
        imgbefore_res.setPixmap(QPixmap(self.imageBefore_path))
        imgbefore_res.setScaledContents(True)
        layout1.addWidget(imgbefore_res)
        groupbox1.setLayout(layout1)

        # 时相二
        groupbox2 = QGroupBox('参考图像: 时相二', hbox)
        layout2 = QHBoxLayout(groupbox2)
        imgafter_res = QLabel(self)
        if self.imageAfter_path is None:
            self.imageAfter_path = r'img/after.png'
        imgafter_res.setPixmap(QPixmap(self.imageAfter_path))
        imgafter_res.setScaledContents(True)
        layout2.addWidget(imgafter_res)
        groupbox2.setLayout(layout2)

        # 监测结果
        self.groupbox3 = QGroupBox('绘制变化区域', hbox)
        layout3 = QHBoxLayout(self.groupbox3)
        # self.cd_res = QLabel()
        self.cd_res = MyLabel()
        # self.cd_res.resize(300, 300)
        # if self.changeResult_path is None:
        #     self.changeResult_path = r'img/label.png'
        # self.cd_res.setPixmap(QPixmap(self.changeResult_path))
        # self.cd_res.setScaledContents(True)
        self.cd_res.setCursor(Qt.CrossCursor)
        layout3.addWidget(self.cd_res)
        self.groupbox3.setLayout(layout3)
        # print('shixianger', imgbefore_res.width(), imgbefore_res.height())
        # print('shixiangyi', imgafter_res.width(), imgafter_res.height())
        # print('bianhuajieguo', self.cd_res.width(), self.cd_res.height())
        # print(self.cd_res.pixmap().size())

        # 添加布局
        imageslayout.addWidget(groupbox1, 1, 1, 1, 1)
        imageslayout.addWidget(groupbox2, 1, 2, 1, 1)
        imageslayout.addWidget(self.groupbox3, 1, 3, 1, 1)
        hbox.setLayout(imageslayout)
        # 返回布局对象
        return hbox

    def getColor(self):
        color = QColorDialog.getColor()
        self.cd_res.color = color
        # p = QPalette()
        # p.setColor(QPalette.WindowText, color)

    def setPenwidth(self):
        items = (str(x) for x in range(1, 50))
        dialog = QInputDialog()
        dialog.resize(400, 400)
        item, ok = dialog.getItem(self, '画笔选项', '宽度设置:', items)
        if ok and item:
            self.cd_res.penwidth = int(item)

    def erase(self):
        self.cd_res.color = Qt.black

    def draw(self):
        self.cd_res.color = Qt.white


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/icon.png'))
    window = DrawWindow('img/after.png')
    window.show()

    sys.exit(app.exec_())
