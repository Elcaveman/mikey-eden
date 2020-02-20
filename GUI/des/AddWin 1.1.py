# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(843, 271)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 210, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Name = QtWidgets.QLineEdit(Dialog)
        self.Name.setGeometry(QtCore.QRect(260, 90, 471, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        self.Name.setFont(font)
        self.Name.setText("")
        self.Name.setMaxLength(100)
        self.Name.setDragEnabled(True)
        self.Name.setObjectName("Name")
        self.BGR = QtWidgets.QLabel(Dialog)
        self.BGR.setGeometry(QtCore.QRect(-10, -60, 1081, 611))
        self.BGR.setText("")
        self.BGR.setPixmap(QtGui.QPixmap("../Images/5a5bc86106b11_thumb900.jpg"))
        self.BGR.setObjectName("BGR")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(18, 80, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Rainbow Bridge Personal Use")
        font.setPointSize(34)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.RadioUrl = QtWidgets.QRadioButton(Dialog)
        self.RadioUrl.setGeometry(QtCore.QRect(740, 90, 111, 31))
        self.RadioUrl.setObjectName("RadioUrl")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(740, 130, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.BGR.raise_()
        self.buttonBox.raise_()
        self.Name.raise_()
        self.label1.raise_()
        self.RadioUrl.raise_()
        self.radioButton.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add proto 1.1"))
        self.label1.setText(_translate("Dialog", "Show Name"))
        self.RadioUrl.setText(_translate("Dialog", "URL"))
        self.radioButton.setText(_translate("Dialog", "See results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

