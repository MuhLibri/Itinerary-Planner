# ketika anda mengklik kolom ubah, maka anda masuk kesini


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        #Dialog.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 80))
        self.frame.setStyleSheet("background-color: rgb(42, 174, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(10, 10, 60, 50))
        self.closeButton.setStyleSheet("QPushButton{\n"
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
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 15, 260, 50))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(42, 174, 255);\n"
"font: 16pt;\n"
"color: white;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 641, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setGeometry(QtCore.QRect(560, 330, 50, 50))
        self.submitButton.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(150, 150, 150);\n"
"border-color: rgb(42, 174, 255);\n"
"font: 16pt;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(116, 116, 116);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0,0,0);\n"
"}")
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(True)
        self.submitButton.setObjectName("submitButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(40, 20, 531, 281))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.addDaerahWisata = QtWidgets.QLineEdit(self.frame_3)
        self.addDaerahWisata.setGeometry(QtCore.QRect(10, 10, 500, 30))
        self.addDaerahWisata.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.addDaerahWisata.setClearButtonEnabled(True)
        self.addDaerahWisata.setObjectName("addDaerahWisata")
        self.addObjekWisata = QtWidgets.QLineEdit(self.frame_3)
        self.addObjekWisata.setGeometry(QtCore.QRect(10, 60, 500, 30))
        self.addObjekWisata.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.addObjekWisata.setClearButtonEnabled(True)
        self.addObjekWisata.setObjectName("addObjekWisata")
        self.tanggalKunjunganDate = QtWidgets.QDateEdit(self.frame_3)
        self.tanggalKunjunganDate.setGeometry(QtCore.QRect(140, 110, 370, 30))
        self.tanggalKunjunganDate.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid black;\n"
"background-color : white;\n"
"padding : 5px;\n"
"    border-left-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}")
        self.tanggalKunjunganDate.setAlignment(QtCore.Qt.AlignCenter)
        self.tanggalKunjunganDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.tanggalKunjunganDate.setObjectName("tanggalKunjunganDate")
        self.addTransportasi = QtWidgets.QLineEdit(self.frame_3)
        self.addTransportasi.setGeometry(QtCore.QRect(10, 200, 500, 30))
        self.addTransportasi.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.addTransportasi.setClearButtonEnabled(True)
        self.addTransportasi.setObjectName("addTransportasi")
        self.tanggalKunjunganLabel = QtWidgets.QLabel(self.frame_3)
        self.tanggalKunjunganLabel.setGeometry(QtCore.QRect(10, 110, 131, 30))
        self.tanggalKunjunganLabel.setStyleSheet("QLabel{\n"
"border-Left: 2px solid black;\n"
"border-Top: 2px solid black;\n"
"border-Bottom: 2px solid black;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"}")
        self.tanggalKunjunganLabel.setObjectName("tanggalKunjunganLabel")
        self.tanggalSelesaiDate = QtWidgets.QDateEdit(self.frame_3)
        self.tanggalSelesaiDate.setGeometry(QtCore.QRect(140, 155, 370, 30))
        self.tanggalSelesaiDate.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid black;\n"
"background-color : white;\n"
"padding : 5px;\n"
"    border-left-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}")
        self.tanggalSelesaiDate.setAlignment(QtCore.Qt.AlignCenter)
        self.tanggalSelesaiDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.tanggalSelesaiDate.setObjectName("tanggalSelesaiDate")
        self.tanggalSelesaiLabel = QtWidgets.QLabel(self.frame_3)
        self.tanggalSelesaiLabel.setGeometry(QtCore.QRect(10, 155, 131, 30))
        self.tanggalSelesaiLabel.setStyleSheet("QLabel{\n"
"border-Left: 2px solid black;\n"
"border-Top: 2px solid black;\n"
"border-Bottom: 2px solid black;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"}")
        self.tanggalSelesaiLabel.setObjectName("tanggalSelesaiLabel")
        self.addDaerahWisata.raise_()
        self.addObjekWisata.raise_()
        self.addTransportasi.raise_()
        self.tanggalKunjunganDate.raise_()
        self.tanggalKunjunganLabel.raise_()
        self.tanggalSelesaiDate.raise_()
        self.tanggalSelesaiLabel.raise_()
        self.frame_3.raise_()
        self.submitButton.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.closeButton.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Ubah Itinerary Planner"))
        self.submitButton.setText(_translate("Dialog", "+"))
        self.addDaerahWisata.setPlaceholderText(_translate("Dialog", "Masukkan Daerah Wisata"))
        self.addObjekWisata.setPlaceholderText(_translate("Dialog", "Masukkan Objek Wisata"))
        self.addTransportasi.setPlaceholderText(_translate("Dialog", "Pilih Transportasi"))
        self.tanggalKunjunganLabel.setText(_translate("Dialog", "Tanggal Kunjungan:"))
        self.tanggalSelesaiLabel.setText(_translate("Dialog", "Tanggal Selesai:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
