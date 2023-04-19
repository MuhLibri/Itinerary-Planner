# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TambahCatatanDialogue.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CatatanWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 801, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("background-color: rgb(42, 174, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 60, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: white;\n"
"    background-color: rgb(42, 174, 255);\n"
"    border: none;\n"
"font: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(35, 148, 213);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(25, 105, 152);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 10, 371, 50))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(42, 174, 255);\n"
"font: 16pt;\n"
"color: white;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, 70, 801, 531))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(350, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 110, 671, 331))
        self.plainTextEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 20px;\n"
"border-color: rgb(42, 174, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 460, 131, 41))
        self.pushButton_2.setStyleSheet("border: none;\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 174, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Tambah Catatan"))
        self.label_2.setText(_translate("MainWindow", "Catatan"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())