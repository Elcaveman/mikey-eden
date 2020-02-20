# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 476)
        self.BGR = QtWidgets.QLabel(Dialog)
        self.BGR.setGeometry(QtCore.QRect(0, -15, 761, 801))
        self.BGR.setText("")
        self.BGR.setPixmap(QtGui.QPixmap("../Images/011.jpg"))
        self.BGR.setObjectName("BGR")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(710, 0, 20, 481))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.title1 = QtWidgets.QLabel(Dialog)
        self.title1.setGeometry(QtCore.QRect(20, 50, 451, 61))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title1.setFont(font)
        self.title1.setObjectName("title1")
        self.watch1 = QtWidgets.QPushButton(Dialog)
        self.watch1.setGeometry(QtCore.QRect(490, 70, 93, 28))
        self.watch1.setObjectName("watch1")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(610, 70, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.watch1_2 = QtWidgets.QPushButton(Dialog)
        self.watch1_2.setGeometry(QtCore.QRect(490, 140, 93, 28))
        self.watch1_2.setObjectName("watch1_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(610, 140, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.title1_2 = QtWidgets.QLabel(Dialog)
        self.title1_2.setGeometry(QtCore.QRect(20, 120, 451, 61))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title1_2.setFont(font)
        self.title1_2.setObjectName("title1_2")
        self.watch1_3 = QtWidgets.QPushButton(Dialog)
        self.watch1_3.setGeometry(QtCore.QRect(490, 210, 93, 28))
        self.watch1_3.setObjectName("watch1_3")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(610, 210, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.title1_3 = QtWidgets.QLabel(Dialog)
        self.title1_3.setGeometry(QtCore.QRect(20, 190, 451, 61))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title1_3.setFont(font)
        self.title1_3.setObjectName("title1_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title1.setText(_translate("Dialog", "Title 1"))
        self.watch1.setText(_translate("Dialog", "Open"))
        self.radioButton.setText(_translate("Dialog", "Delete"))
        self.watch1_2.setText(_translate("Dialog", "Open"))
        self.radioButton_2.setText(_translate("Dialog", "Delete"))
        self.title1_2.setText(_translate("Dialog", "Title 1"))
        self.watch1_3.setText(_translate("Dialog", "Open"))
        self.radioButton_3.setText(_translate("Dialog", "Delete"))
        self.title1_3.setText(_translate("Dialog", "Title 1"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

