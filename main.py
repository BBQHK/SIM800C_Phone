from __future__ import print_function
from subprocess import call
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from SIM800C_PhoneCallUI import *
from phoneCall import connect_SIM800C, calling, cut_off
import threading

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        # create a attribute for SIM800C
        self.SIM800C = connect_SIM800C('USB-SERIAL')

        self.setWindowIcon(QtGui.QIcon('./asset/icon.jpg'))
        self.setupUi(self)
        self.pushButton_0.clicked.connect(partial(self.btn_0_function))
        self.pushButton_1.clicked.connect(partial(self.btn_1_function))
        self.pushButton_2.clicked.connect(partial(self.btn_2_function))
        self.pushButton_3.clicked.connect(partial(self.btn_3_function))
        self.pushButton_4.clicked.connect(partial(self.btn_4_function))
        self.pushButton_5.clicked.connect(partial(self.btn_5_function))
        self.pushButton_6.clicked.connect(partial(self.btn_6_function))
        self.pushButton_7.clicked.connect(partial(self.btn_7_function))
        self.pushButton_8.clicked.connect(partial(self.btn_8_function))
        self.pushButton_9.clicked.connect(partial(self.btn_9_function))
        self.pushButton_10.clicked.connect(partial(self.btn_10_function))
        self.pushButton_11.clicked.connect(partial(self.btn_11_function))
        self.pushButton_12.clicked.connect(partial(self.btn_call_function))
        self.pushButton_13.clicked.connect(partial(self.btn_cutOff_function))
        self.pushButton_del.clicked.connect(partial(self.btn_delText_function))

    def btn_0_function(self):
        self.lineEdit.insert("0")
    def btn_1_function(self):
        self.lineEdit.insert("1")
    def btn_2_function(self):
        self.lineEdit.insert("2")
    def btn_3_function(self):
        self.lineEdit.insert("3")
    def btn_4_function(self):
        self.lineEdit.insert("4")
    def btn_5_function(self):
        self.lineEdit.insert("5")
    def btn_6_function(self):
        self.lineEdit.insert("6")
    def btn_7_function(self):
        self.lineEdit.insert("7")
    def btn_8_function(self):
        self.lineEdit.insert("8")
    def btn_9_function(self):
        self.lineEdit.insert("9")
    def btn_10_function(self):
        self.lineEdit.insert("*")
    def btn_11_function(self):
        self.lineEdit.insert("#")

    def btn_call_function(self):
        print("Calling to " + self.lineEdit.text())
        t1 = threading.Thread(target=calling, args=(self.lineEdit.text(), self.SIM800C))
        t1.start()
        
    def btn_cutOff_function(self):
        cut_off(self.SIM800C)

    def btn_delText_function(self):
        self.lineEdit.setText(self.lineEdit.text()[0:-1])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())