# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
class AddWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("Add proto 1.0")
        self.setGeometry(50,30,843, 271)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(360, 210, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.Name = QtWidgets.QLineEdit(self)
        self.Name.setGeometry(QtCore.QRect(280, 90, 451, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        self.Name.setFont(font)
        self.Name.setText("")
        self.Name.setMaxLength(100)
        self.Name.setDragEnabled(True)

        self.BGR = QtWidgets.QLabel(self)
        self.BGR.setGeometry(QtCore.QRect(-10, -60, 1081, 611))
        self.BGR.setText("")
        self.BGR.setPixmap(QtGui.QPixmap("Images/5a5bc86106b11_thumb900.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(18, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Rainbow Bridge Personal Use")
        font.setPointSize(34)
        self.label1.setFont(font)

        self.RadioUrl = QtWidgets.QRadioButton(self)
        self.RadioUrl.setGeometry(QtCore.QRect(760, 110, 111, 31))

        self.BGR.raise_()
        self.buttonBox.raise_()
        self.Name.raise_()
        self.label1.raise_()
        self.RadioUrl.raise_()

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        
        self.label1.setText("Show Name")
        self.RadioUrl.setText("URL")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AddWin()
    ui.show()
    sys.exit(app.exec_())

