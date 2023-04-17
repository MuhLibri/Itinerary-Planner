import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from ui_RiwayatInterface import *

class MainWindow(QMainWindow):
    riwayatCount = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Riwayat()
        self.ui.setupUi(self)
        self.show()

        self.ui.pushButton_2.clicked.connect(self.createNewWidget)

        #self.createNewWidget()
    
    def createNewWidget(self):
        newRiwayat = "riwayatFrame" + str(self.riwayatCount)
        newVertical = "verticalName" + str(self.riwayatCount)
        newTitle = "title" + str(self.riwayatCount)
        newDuration = "duration" + str(self.riwayatCount)
        newDestination = "destination" + str(self.riwayatCount)
        newUbah = "ubah" + str(self.riwayatCount)
        newCatatan = "catatan" + str(self.riwayatCount)
        self.riwayatCount += 1

        self.frame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 150))
        self.frame_2.setMaximumSize(QtCore.QSize(800, 150))
        self.frame_2.setStyleSheet("#" + newRiwayat + "{\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(newRiwayat)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(newVertical)
        self.TitleLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        #Setup title
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(newTitle)
        self.TitleLabel.setText(newTitle)
        self.verticalLayout_4.addWidget(self.TitleLabel)
        

        #Setup duration
        self.DurationLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DurationLabel.setFont(font)
        self.DurationLabel.setObjectName(newDuration)
        self.DurationLabel.setText(newDuration)
        self.verticalLayout_4.addWidget(self.DurationLabel)

        #Setup destination
        self.DestinationLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DestinationLabel.setFont(font)
        self.DestinationLabel.setObjectName(newDestination)
        self.DestinationLabel.setText(newDestination)
        self.verticalLayout_4.addWidget(self.DestinationLabel)

        #Setup ubah
        self.UbahLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.UbahLabel.setFont(font)
        self.UbahLabel.setStyleSheet("color:rgb(12, 190, 255)")
        self.UbahLabel.setObjectName(newUbah)
        self.UbahLabel.setText("Ubah")
        self.verticalLayout_4.addWidget(self.UbahLabel)

        #Setup catatan
        self.CatatanLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.CatatanLabel.setFont(font)
        self.CatatanLabel.setStyleSheet("color:rgb(12, 190, 255)")
        self.CatatanLabel.setObjectName(newCatatan)
        self.CatatanLabel.setText("Catatan")
        self.verticalLayout_4.addWidget(self.CatatanLabel)

        self.ui.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(750, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(750, 100))
        self.frame_2.setStyleSheet("background-color: white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(newRiwayat)
        self.ui.verticalLayout_3.addWidget(self.frame_2)

        setattr(self.ui, newRiwayat, self.frame_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
