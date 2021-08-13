# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trail.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(520, 490, 112, 34))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(660, 490, 112, 34))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.toolButton = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton.setGeometry(QtCore.QRect(100, 40, 52, 24))
#         self.toolButton.setObjectName("toolButton")
#         self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
#         self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 140, 160, 271))
#         self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.dial = QtWidgets.QDial(self.verticalLayoutWidget)
#         self.dial.setObjectName("dial")
#         self.verticalLayout.addWidget(self.dial)
#         self.timeEdit = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
#         self.timeEdit.setObjectName("timeEdit")
#         self.verticalLayout.addWidget(self.timeEdit)
#         self.line = QtWidgets.QFrame(self.centralwidget)
#         self.line.setGeometry(QtCore.QRect(30, 200, 118, 3))
#         self.line.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line.setObjectName("line")
#         self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar.setGeometry(QtCore.QRect(40, 490, 120, 23))
#         self.progressBar.setProperty("value", 24)
#         self.progressBar.setObjectName("progressBar")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(240, 30, 121, 81))
#         self.label.setObjectName("label")
#         self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit.setGeometry(QtCore.QRect(410, 140, 221, 271))
#         self.textEdit.setObjectName("textEdit")
#         self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
#         self.spinBox.setGeometry(QtCore.QRect(390, 60, 49, 25))
#         self.spinBox.setObjectName("spinBox")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(640, 60, 112, 34))
#         self.pushButton_3.setObjectName("pushButton_3")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
#         self.menubar.setObjectName("menubar")
#         self.menu = QtWidgets.QMenu(self.menubar)
#         self.menu.setObjectName("menu")
#         self.menu_2 = QtWidgets.QMenu(self.menubar)
#         self.menu_2.setObjectName("menu_2")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.actiona = QtWidgets.QAction(MainWindow)
#         self.actiona.setObjectName("actiona")
#         self.actiondakai = QtWidgets.QAction(MainWindow)
#         self.actiondakai.setObjectName("actiondakai")
#         self.actionguanbi = QtWidgets.QAction(MainWindow)
#         self.actionguanbi.setObjectName("actionguanbi")
#         self.actionclose = QtWidgets.QAction(MainWindow)
#         self.actionclose.setObjectName("actionclose")
#         self.menu.addAction(self.actiona)
#         self.menu.addAction(self.actionclose)
#         self.menu_2.addAction(self.actiondakai)
#         self.menu_2.addAction(self.actionguanbi)
#         self.menubar.addAction(self.menu.menuAction())
#         self.menubar.addAction(self.menu_2.menuAction())
#
#         self.retranslateUi(MainWindow)
#         self.pushButton_2.clicked.connect(MainWindow.close)
#         self.pushButton.clicked.connect(self.label.clear)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "OK"))
#         self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
#         self.toolButton.setText(_translate("MainWindow", "其他"))
#         self.label.setText(_translate("MainWindow", "label2"))
#         self.pushButton_3.setText(_translate("MainWindow", "print"))
#         self.menu.setTitle(_translate("MainWindow", "文件"))
#         self.menu_2.setTitle(_translate("MainWindow", "项目"))
#         self.actiona.setText(_translate("MainWindow", "open"))
#         self.actiondakai.setText(_translate("MainWindow", "dakai"))
#         self.actionguanbi.setText(_translate("MainWindow", "guanbi"))
#         self.actionclose.setText(_translate("MainWindow", "close"))


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox('On and Off', self)  # 1
        self.groupbox_2 = QGroupBox('Change Color', self)

        self.red = QRadioButton('Red', self)  # 2
        self.blue = QRadioButton('Blue', self)
        self.green = QRadioButton('Green', self)
        self.yellow = QRadioButton('Yellow', self)
        self.color_list = [self.red, self.blue, self.green, self.yellow]

        self.on = QRadioButton('On', self)  # 3
        self.off = QRadioButton('Off', self)

        self.pic_label = QLabel(self)  # 4

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        self.groupbox_1.setLayout(self.h1_layout)

        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_v_layout.addWidget(self.pic_label)
        self.all_v_layout.addLayout(self.h3_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.yellow.setChecked(True)  # 5
        [btn.clicked.connect(self.change_color_func) for btn in self.color_list]

        self.off.setChecked(True)  # 6
        self.off.toggled.connect(self.on_and_off_func)

    def label_init(self):  # 7
        self.pic_label.setPixmap(QPixmap('images/Off.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

    def change_color_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))

    def on_and_off_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap('images/Off.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())