# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import cv2
import numpy as np
import os
import random

from drawWin import DrawWindow


class ChangeDetectionMainWin(QWidget):
    def __init__(self):
        super(ChangeDetectionMainWin, self).__init__()
        self.setUIGeometry()  # 设置主窗口布局
        self.initUI()

        self.imageBefore_path = None
        self.imageAfter_path = None
        self.changeResult_path = 'img/background.png'
        self.cd_category = None
        self.area = None

        self.cd_pic_id = None

        self.flag = False

    def setUIGeometry(self):
        """
        设置主窗口居中布局，尺寸大小
        """
        # 设置标题
        self.setWindowTitle('基于变化检测的自然资源检测综合系统')
        # 设置尺寸
        width = 1500
        height = 950
        self.resize(width, height)
        size = self.geometry()
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 移动窗口
        x = int((screen.width()-size.width()-200)/2)
        y = int((screen.height()-size.height()-80)/2)
        self.move(x, y)

    def initUI(self):
        # 设置全局的栅格布局
        globLayout = QGridLayout(self)
        # btn 按钮
        self.tools = self.toolBtns()
        globLayout.addWidget(self.tools, 1, 1, 1, 2)
        # image pair 图像对
        self.imgpairs = self.imgPair()
        globLayout.addWidget(self.imgpairs, 2, 1, 3, 2)
        # 变化检测结果显示
        self.cdResult = self.cdResultShow()
        globLayout.addWidget(self.cdResult, 5, 1, 3, 2)
        # map 地图
        self.map = self.mapShow()
        globLayout.addWidget(self.map, 1, 3, 7, 7)
        # table 表格
        self.table = self.tableShow()
        globLayout.addWidget(self.table, 1, 10, 7, 1)

        # 变化监测结果记录
        self.textRecord = self.recordShow_1()
        globLayout.addWidget(self.textRecord, 8, 1, 1, 2)
        # 统计结果记录
        self.textRecord = self.recordShow_2()
        globLayout.addWidget(self.textRecord, 8, 3, 1, 7)
        # 统计结果记录
        self.textRecord = self.recordShow_3()
        globLayout.addWidget(self.textRecord, 8, 10, 1, 7)

        # 添加状态栏
        # self.statusbar = QStatusBar()
        # globLayout.addWidget(self.statusbar, 3, 1, 7, 1)

        self.setLayout(globLayout)

    def toolBtns(self):
        # 用于接收布局的对象
        hbox = QGroupBox('操作按钮', self)
        # 设置布局
        toolBtnslayout = QHBoxLayout(hbox)
        # 导入文件夹导入
        zidongBtn = QPushButton('选择文件夹', self)
        toolBtnslayout.addWidget(zidongBtn, alignment=Qt.AlignCenter)
        zidongBtn.clicked.connect(self.loadDir)
        # 选择图像导入
        chooseBtn = QPushButton('选择图像', self)
        toolBtnslayout.addWidget(chooseBtn, alignment=Qt.AlignCenter)
        chooseBtn.clicked.connect(self.loadImage)
        # 检测按钮
        jianceBtn = QPushButton('变化检测', self)
        toolBtnslayout.addWidget(jianceBtn, alignment=Qt.AlignCenter)
        jianceBtn.clicked.connect(self.jiance)
        # 添加布局
        self.setLayout(toolBtnslayout)
        # 返回布局对象
        return hbox

    def imgPair(self):
        # 设置窗口对象
        vbox = QGroupBox('待检测图像',self)
        # 设置布局
        imgPairlayout = QGridLayout(vbox)
        # 时相1 图像名称
        imageBeforeTitle = QLabel('时相一:', vbox)
        imageBeforeTitle.resize(10, 10)
        imageBeforeTitle.setScaledContents(True)
        imgPairlayout.addWidget(imageBeforeTitle, 1, 1, 2, 1, alignment=Qt.AlignCenter)

        # 时相1 图像
        self.imageBefore = QLabel('时相1：',)
        self.imageBefore.setPixmap(QPixmap(r'img/loading.png'))
        self.imageBefore.setScaledContents(True)
        imgPairlayout.addWidget(self.imageBefore, 1, 2, 2, 2)  # , alignment=Qt.AlignCenter)

        # 时相2 图像名称
        imageAfterTitle = QLabel('时相二：', vbox)
        imgPairlayout.addWidget(imageAfterTitle, 3, 1, 2, 1, alignment=Qt.AlignCenter)
        # 时相2 图像
        self.imageAfter = QLabel('时相2')
        self.imageAfter.setPixmap(QPixmap(r'img/loading.png'))
        self.imageAfter.setScaledContents(True)
        imgPairlayout.addWidget(self.imageAfter, 3, 2, 2, 2) # , alignment=Qt.AlignCenter)
        # 添加布局
        vbox.setLayout(imgPairlayout)
        # 返回对象
        return vbox

    def mapShow(self):
        # 设置窗口对象
        mapwidget = QGroupBox('地理数据可视化', self)
        # 设置布局
        mapLayout = QVBoxLayout()
        # 设置图像
        changeMap = QLabel(mapwidget)
        changeMap.setPixmap(QPixmap(r'img/map.png'))
        changeMap.setScaledContents(True)
        mapLayout.addWidget(changeMap)
        # 添加布局
        mapwidget.setLayout(mapLayout)

        return mapwidget

    def cdResultShow(self):
        # 设置窗口对象
        reswidget = QGroupBox('变化检测结果', self)
        # 设置布局
        resLayout = QGridLayout()
        # 添加属性调整按钮
        catBtn = QPushButton('类别')
        resLayout.addWidget(catBtn, 1, 1, 1, 1)
        catBtn.clicked.connect(self.getItem)
        # 添加绘制按钮
        drawBtn = QPushButton('绘制')
        resLayout.addWidget(drawBtn, 2, 1, 1, 1)
        drawBtn.clicked.connect(self.drawArea)
        # 添加按钮
        setokBtn = QPushButton('确认')
        resLayout.addWidget(setokBtn, 3, 1, 1, 1)
        setokBtn.clicked.connect(self.okDraw)
        # 取消按钮
        resumeBtn = QPushButton('恢复')
        resLayout.addWidget(resumeBtn, 4, 1, 1, 1)
        resumeBtn.clicked.connect(self.Resume)
        # 设置图像
        self.changeMap = QLabel(reswidget)
        self.changeMap.setPixmap(QPixmap(r'img/background.png'))
        self.changeMap.setScaledContents(True)
        resLayout.addWidget(self.changeMap, 1, 2, 4, 4)
        # 添加布局
        reswidget.setLayout(resLayout)

        return reswidget

    def recordShow_1(self):
        # 设置窗口对象
        reswidget = QGroupBox('变化区域类型记录', self)
        # 设置布局
        resLayout = QGridLayout(reswidget)
        # 结果显示
        self.textShow_1 = QTextEdit(reswidget)
        self.textShow_1.setText('#变化区域属性#')
        resLayout.addWidget(self.textShow_1)
        # 添加布局
        reswidget.setLayout(resLayout)

        return reswidget

    def recordShow_2(self):
        # 设置窗口对象
        reswidget = QGroupBox('数据分析结果', self)
        # 设置布局
        resLayout = QGridLayout(reswidget)
        # 结果显示
        self.textShow_2 = QTextEdit(reswidget)
        self.textShow_2.setText('#数据分析#')
        resLayout.addWidget(self.textShow_2)
        # 添加布局
        reswidget.setLayout(resLayout)

        return reswidget

    def recordShow_3(self):
        # 设置窗口对象
        reswidget = QGroupBox('统计结果记录', self)
        # 设置布局
        resLayout = QGridLayout(reswidget)
        # 结果显示
        self.textShow_3 = QTextEdit(reswidget)
        self.textShow_3.resize(300, 100)
        self.textShow_3.setText('#统计结果#')
        resLayout.addWidget(self.textShow_3)
        # 添加布局
        reswidget.setLayout(resLayout)

        return reswidget

    def tableShow(self):
        # 设置窗口对象
        tablewidget = QGroupBox('统计结果', self)
        # 设置布局
        tableLayout = QGridLayout()
        # 图像
        table_image1 = QPixmap(r'img/table1.png')
        table_image1 = table_image1.scaled(400,200)
        # 设置图像
        tableMap1 = QLabel(tablewidget)
        tableMap1.setPixmap(table_image1)
        tableMap1.setScaledContents(True)
        tableLayout.addWidget(tableMap1, 1, 1, 1, 1)

        # 图像
        table_image2 = QPixmap(r'img/table2.png')
        table_image2 = table_image2.scaled(400, 200)
        # 设置图像
        tableMap2 = QLabel(tablewidget)
        tableMap2.setPixmap(QPixmap(table_image2))
        tableMap2.setScaledContents(True)
        tableLayout.addWidget(tableMap2, 2, 1, 1, 1)

        # 图像
        table_image3 = QPixmap(r'img/table3.png')
        table_image3 = table_image3.scaled(400, 200)
        # 设置图像
        tableMap3 = QLabel(tablewidget)
        tableMap3.setPixmap(QPixmap(table_image3))
        tableMap3.setScaledContents(True)
        tableLayout.addWidget(tableMap3, 3, 1, 1, 1)
        # 添加布局
        tablewidget.setLayout(tableLayout)

        return tablewidget

    # signals and slots
    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', './demo/B', '图像文件(*.jpg *.png)')
        image = QPixmap(fname)
        image.scaled(self.imageAfter.width(), self.imageAfter.height())
        self.imageAfter.setPixmap(image)

        self.imageAfter_path = fname
        # self.imageBefore.setScaledContents(True)

        image = QPixmap(os.path.join(r'F:\MyWork\Programming\PyQT_UI\ChangeDetection_UI\demo\A\\', fname.split('/')[-1]))
        self.cd_pic_id = fname.split('/')[-1]
        image_path = os.path.join(r'F:\MyWork\Programming\PyQT_UI\ChangeDetection_UI\demo\A', fname.split('/')[-1])
        self.imageBefore.setPixmap(image)

        self.imageBefore_path = image_path

    def loadDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹")  # 起始路径
        if dir_choose == "":
            print("\n取消选择")
        print("\n你选择的文件夹为:", dir_choose)

    def drawArea(self):
        self.form1 = DrawWindow(self.imageBefore_path, self.imageAfter_path, self.changeResult_path)
        self.form1.show()
        self.form1.exec()
        if True:
            self.changeMap.setPixmap(self.form1.cd_res.pixmap().scaled(128, 128))
            self.flag = True

    def okDraw(self):
        if self.flag:
            self.changeResult_path = 'pixmap.png'
            self.form1.cd_res.pixmap().scaled(128, 128).save('pixmap.png')
            reply = QMessageBox.information(self, '提示', '图片已保存!', QMessageBox.Yes | QMessageBox.Yes, QMessageBox.No)
        else:
            self.changeResult_path = 'img/label.png'
            QMessageBox.information(self, '提示', '图片未修改, 无需重新保存!', QMessageBox.Yes | QMessageBox.Yes, QMessageBox.No)

        tmp_img = cv2.imread(self.changeResult_path, 0)
        self.area = int(np.sum(tmp_img)/255)
        self.image_shape = tmp_img.shape
        self.whole_area = int(tmp_img.shape[0]*tmp_img.shape[1])

        show_str = '变化图像路径：{},\n图像大小：{}，\n变化区域类型：{},\n'.format(
            self.changeResult_path, self.image_shape, self.cd_category, self.area, self.whole_area)
        self.textShow_1.setText(show_str)

        show_str = '变化区域面积：{}/{}.\n'.format(
            self.area, self.whole_area)
        self.textShow_2.setText(show_str)

        show_str = '2019年{}面积(公顷)：{}，\n2020年{}面积(公顷)：{}，\n2021年{}面积(公顷)：{},\n'.format(
            self.cd_category, int(self.area * (0.5 + random.random())),
            self.cd_category, int(self.area * (0.5 + random.random())),
            self.cd_category, int(self.area * (0.5 + random.random())))
        self.textShow_3.setText(show_str)

    def getItem(self):
        items = ('建筑', '林地', '耕地', '水域')
        dialog = QInputDialog()
        dialog.resize(400, 400)
        item, ok = dialog.getItem(self, '变化类型', '用地类型:', items)
        if ok and item:
            self.cd_category = item

    def Resume(self):
        if self.changeResult_path is None:
            self.changeResult_path = r'img/label.png'

        self.changeMap.setPixmap(QPixmap(self.changeResult_path))

        tmp_img = cv2.imread(self.changeResult_path, 0)
        self.area = int(np.sum(tmp_img) / 255)
        self.image_shape = tmp_img.shape
        self.whole_area = int(tmp_img.shape[0] * tmp_img.shape[1])

        show_str = '变化图像路径：{},\n图像大小：{}，\n变化区域类型：{},\n变化区域面积：{}/{}.\n'.format(
            self.changeResult_path, self.image_shape, self.cd_category, self.area, self.whole_area)
        self.textShow_1.setText(show_str)

    def jiance(self):
        if self.cd_pic_id is not None:
            image_path = os.path.join(r'F:\MyWork\Programming\PyQT_UI\ChangeDetection_UI\demo\pred', self.cd_pic_id.replace('.jpg', '.png'))
            self.changeResult_path = image_path
            image = QPixmap(image_path)
            self.changeMap.setPixmap(image)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/icon.png'))
    window = ChangeDetectionMainWin()
    window.show()

    sys.exit(app.exec_())







