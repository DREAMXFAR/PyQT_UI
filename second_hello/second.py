# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from second_hello.trail import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.printit)
        self.actiona.triggered.connect(self.a)

    def printit(self):
        print('按钮被按下')
        self.label.setText(u'修改文本框内容测试成功啦')
        return 0

    def a(self):
        self.label.setText(u'click a')
        return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setWindowTitle('Hello PyQt5')
    myWin.show()
    sys.exit(app.exec_())




