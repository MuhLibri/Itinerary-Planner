# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DaerahWisataInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Database

class Ui_DaerahWisata(object):
    daerahWisataTable=Database.Database.search("Daerah")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 80, 801, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 80))
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
        self.label.setGeometry(QtCore.QRect(220, 0, 371, 50))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(42, 174, 255);\n"
"font: 16pt;\n"
"color: white;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 47, 93, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: white;\n"
"    background-color: rgb(42, 174, 255);\n"
"    border: none;\n"
"font: 10pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(35, 148, 213);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(25, 105, 152);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 641, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_2.clicked.connect(self.searchButtonClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for e in self.daerahWisataTable:
            self.createNewWidget(e[0],e[1])

    def createNewWidget(self,namaDaerahWisata,informasiDaerahWisata):
        newDaerahWisata="daerahWisataFrame"+str(len(self.daerahWisataTable))
        newVertical="verticalName"+str(len(self.daerahWisataTable))
        newNamaDaerahWisata=namaDaerahWisata
        newInformasiDaerahWisata=informasiDaerahWisata

        self.daerahWisataFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daerahWisataFrame.sizePolicy().hasHeightForWidth())
        self.daerahWisataFrame.setSizePolicy(sizePolicy)
        self.daerahWisataFrame.setMinimumSize(QtCore.QSize(800, 150))
        self.daerahWisataFrame.setMaximumSize(QtCore.QSize(800, 150))
        self.daerahWisataFrame.setStyleSheet("#"+newDaerahWisata+"{\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"}")
        self.daerahWisataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.daerahWisataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.daerahWisataFrame.setObjectName(newDaerahWisata)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.daerahWisataFrame)
        self.verticalLayout.setObjectName(newVertical)
        self.namaDaerahWisataLabel = QtWidgets.QLabel(self.daerahWisataFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.namaDaerahWisataLabel.setFont(font)
        self.namaDaerahWisataLabel.setObjectName(newNamaDaerahWisata)
        self.namaDaerahWisataLabel.setText(newNamaDaerahWisata)
        self.verticalLayout.addWidget(self.namaDaerahWisataLabel)

        self.informasiDaerahWisataLabel = QtWidgets.QLabel(self.daerahWisataFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.informasiDaerahWisataLabel.setFont(font)
        self.informasiDaerahWisataLabel.setObjectName(newInformasiDaerahWisata)
        self.informasiDaerahWisataLabel.setText(newInformasiDaerahWisata)
        self.verticalLayout.addWidget(self.informasiDaerahWisataLabel)

        self.verticalLayout_3.addWidget(self.daerahWisataFrame,QtCore.Qt.AlignTop)
        self.daerahWisataFrame=QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.daerahWisataFrame.setMinimumSize(QtCore.QSize(745, 0))
        self.daerahWisataFrame.setMaximumSize(QtCore.QSize(745, 50))
        self.daerahWisataFrame.setStyleSheet("background-color: white;")
        self.daerahWisataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.daerahWisataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.daerahWisataFrame.setObjectName(newDaerahWisata)
        self.verticalLayout_3.addWidget(self.daerahWisataFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.addStretch()
        

        setattr(self,newDaerahWisata,self.daerahWisataFrame)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Daerah Wisata"))
        self.pushButton_2.setText(_translate("MainWindow", "Search!"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Cari Daerah Wisata"))

    def searchButtonClicked(self):
        searchText=self.lineEdit.text()
        for cnt in reversed(range(self.verticalLayout_3.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
                widget = self.verticalLayout_3.takeAt(cnt).widget()

                if widget is not None: 
                    # widget will be None if the item is a layout
                    widget.deleteLater()
        if searchText!="":
            searchedObjekWisata=Database.Database.search("Daerah",NamaDaerah=searchText)
            for el in searchedObjekWisata:
                self.createNewWidget(el[0],el[1])
                self.retranslateUi(MainWindow)
        else:
            for e in self.daerahWisataTable:
                self.createNewWidget(e[0],e[1])
                self.retranslateUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DaerahWisata()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())