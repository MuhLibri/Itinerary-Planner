# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QInputDialog, QTextBrowser
from PyQt5.QtCore import pyqtSlot
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Edit Itinerary Planner')
        self.setGeometry(100, 100, 503, 661)

        widget = QWidget()
        self.setCentralWidget(widget)

        gridLayout = QGridLayout()
        widget.setLayout(gridLayout)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 141))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.label.setText("       Edit Itinerary Planner")

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 150, 256, 121))
        self.textBrowser.setStyleSheet("border-right-color: rgb(0, 0, 0);\n"
"border-color: rgb(85, 0, 255);\n"
"border-top-color: rgb(0, 85, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QTextBrowser(self)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 320, 256, 121))
        self.textBrowser_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton1 = QPushButton('Ubah', self)
        self.pushButton2 = QPushButton('Hapus', self)
        self.pushButton1.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushButton2.setGeometry(QtCore.QRect(140, 280, 75, 23))
        self.pushButton1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton1.clicked.connect(self.ubahTeks)
        self.pushButton2.clicked.connect(self.hapusTeks)

        self.show()

    @pyqtSlot()
    def ubahTeks(self):
        teksBaru, ok = QInputDialog.getText(self, 'Ubah Teks', 'Masukkan teks baru:')
        if ok:
            self.textBrowser.setText(teksBaru)

    @pyqtSlot()
    def hapusTeks(self):
        self.textBrowser.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    sys.exit(app.exec_())
