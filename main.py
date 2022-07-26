from __future__ import print_function
from subprocess import call
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from SIM800C_PhoneCallUI import *
from phoneCall import calling
from multiprocessing import Process

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('phone.jpg'))
        self.setupUi(self)
        self.pushButton_0.clicked.connect(partial(self.btn_0))
        self.pushButton_1.clicked.connect(partial(self.btn_1))
        self.pushButton_2.clicked.connect(partial(self.btn_2))
        self.pushButton_3.clicked.connect(partial(self.btn_3))
        self.pushButton_4.clicked.connect(partial(self.btn_4))
        self.pushButton_5.clicked.connect(partial(self.btn_5))
        self.pushButton_6.clicked.connect(partial(self.btn_6))
        self.pushButton_7.clicked.connect(partial(self.btn_7))
        self.pushButton_8.clicked.connect(partial(self.btn_8))
        self.pushButton_9.clicked.connect(partial(self.btn_9))
        self.pushButton_10.clicked.connect(partial(self.btn_10))
        self.pushButton_11.clicked.connect(partial(self.btn_11))
        self.pushButton_12.clicked.connect(partial(self.call))
        self.pushButton_13.clicked.connect(partial(self.cutOff))
        self.pushButton_del.clicked.connect(partial(self.delText))

    def btn_0(self):
        self.lineEdit.insert("0")
    def btn_1(self):
        self.lineEdit.insert("1")
    def btn_2(self):
        self.lineEdit.insert("2")
    def btn_3(self):
        self.lineEdit.insert("3")
    def btn_4(self):
        self.lineEdit.insert("4")
    def btn_5(self):
        self.lineEdit.insert("5")
    def btn_6(self):
        self.lineEdit.insert("6")
    def btn_7(self):
        self.lineEdit.insert("7")
    def btn_8(self):
        self.lineEdit.insert("8")
    def btn_9(self):
        self.lineEdit.insert("9")
    def btn_10(self):
        self.lineEdit.insert("*")
    def btn_11(self):
        self.lineEdit.insert("#")

    def call(self):
        print("Calling to " + self.lineEdit.text())
        p = Process(target=calling, args=(self.lineEdit.text(),))
        p.start()
        # calling(self.lineEdit.text())
    def cutOff(self):
        print("Cut off")

    def delText(self):
        self.lineEdit.setText(self.lineEdit.text()[0:-1])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())