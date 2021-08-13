# -*- coding:utf-8 -*-
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from helloqt import *
#
#
# class MyWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MyWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.end_Btn.clicked.connect(self.end_event)  # 绑定登陆函数
#
#     # 登陆函数
#     def end_event(self):
#         if self.name_Edit.text() == "":
#             QMessageBox.about(self, '登陆', '请输入姓名')
#         elif self.pass_Edit.text() == "":
#             QMessageBox.about(self, '登陆', '请输入密码')
#         else:
#             QMessageBox.about(self, '登陆', self.name_Edit.text() + ' 欢迎登陆')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWin = MyWindow()
#     myWin.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QMessageBox, QPushButton)
from PyQt5.QtCore import QCoreApplication

# # 主窗体
# app = QApplication(sys.argv)  # 创建应用对象
# LoginWindow = QWidget()  # 构造登陆窗口
# LoginWindow.setWindowTitle('登陆窗口')  # 窗口标题
# LoginWindow.resize(300, 180)  # 窗口大小
#
# # 姓名Label
# name_Label = QLabel(LoginWindow)  # 放置在登陆窗口上
# name_Label.setText('姓名')  # 设置显示文本
# name_Label.move(60, 40)  # 设置位置
#
# # 输入姓名文本框
# name_Edit = QLineEdit(LoginWindow)  # 放置在登陆窗口上
# name_Edit.move(100, 36)  # 设置位置
#
# # 密码Label
# pass_Label = QLabel(LoginWindow)  # 放置在登陆窗口上
# pass_Label.setText('密码')  # 设置显示文本
# pass_Label.move(60, 80)  # 设置位置
#
# # 输入密码文本框
# pass_Edit = QLineEdit(LoginWindow)  # 放置在登陆窗口上
# pass_Edit.move(100, 76)  # 设置位置
# pass_Edit.setEchoMode(QLineEdit.Password)  # 设置输入密码不可见
#
#
# # 登陆函数
# def end_event():
#     if name_Edit.text() == "":
#         QMessageBox.about(LoginWindow, '登陆', '请输入姓名')
#     elif pass_Edit.text() == "":
#         QMessageBox.about(LoginWindow, '登陆', '请输入密码')
#     else:
#         QMessageBox.about(LoginWindow, '登陆', name_Edit.text() + ' 欢迎登陆')
#
#
# # 登陆按钮
# end_Btn = QPushButton('登陆', LoginWindow)
# end_Btn.clicked.connect(end_event)  # 绑定登陆函数
# end_Btn.move(60, 120)
#
# # 退出按钮
# exit_Btn = QPushButton('退出', LoginWindow)
# exit_Btn.clicked.connect(QCoreApplication.instance().quit)  # 绑定退出事件
# exit_Btn.move(160, 120)
#
# LoginWindow.show()  # 显示窗口
# sys.exit(app.exec_())  # 进入消息循环
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("高级控件-QTabWidget容器控件 - PyQt5中文网")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.tab = QTabWidget(self)
        self.tab.resize(500, 400)
        # 创建三个窗口控件
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        # 添加窗口到QTabWidget容器控件
        self.tab.addTab(self.tab1, '窗口一')
        self.tab.addTab(self.tab2, '窗口二')
        self.tab.addTab(self.tab3, '窗口三')
        self.tab_ui1()

    def tab_ui1(self):
        layout = QFormLayout()
        layout.addRow('账号：', QLineEdit())
        layout.addRow('密码：', QLineEdit())
        layout.addRow(QPushButton('点击登陆'))
        self.tab1.setLayout(layout)  # 把布局设置到界面1上面
        self.tab.setTabText(0, '登陆界面')  # 更改界面名称
        self.tab.setTabText(1, '注册界面')
        self.tab.setTabText(2, '找回密码')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

