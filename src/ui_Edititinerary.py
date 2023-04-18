from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(503, 638)
        self.lapisan1 = QtWidgets.QWidget(Form)
        self.lapisan1.setGeometry(QtCore.QRect(0, 0, 501, 661))
        self.lapisan1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lapisan1.setObjectName("lapisan1")
        self.label = QtWidgets.QLabel(self.lapisan1)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 141))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.lapisan1)
        self.textBrowser.setGeometry(QtCore.QRect(10, 150, 256, 121))
        self.textBrowser.setStyleSheet("border-right-color: rgb(0, 0, 0);\n"
"border-color: rgb(85, 0, 255);\n"
"border-top-color: rgb(0, 85, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.lapisan1)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 320, 256, 121))
        self.textBrowser_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.lapisan1)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.lapisan1)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 280, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "       Edit Itinerary Planner"))
        self.pushButton.setText(_translate("Form", "ubah"))
        self.pushButton_2.setText(_translate("Form", "hapus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())