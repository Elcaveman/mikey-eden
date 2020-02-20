# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pixm = QtWidgets.QLabel(self.centralwidget)
        self.pixm.setGeometry(QtCore.QRect(-50, -50, 1201, 821))
        self.pixm.setText("")
        self.pixm.setPixmap(QtGui.QPixmap("../Images/5rc649g05kw11.jpg"))
        self.pixm.setObjectName("pixm")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(130, 120, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.add.setFont(font)
        self.add.setStyleSheet("QPushButton{opacity:20%;}")
        self.add.setObjectName("add")
        self.show = QtWidgets.QPushButton(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(130, 320, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.show.setFont(font)
        self.show.setObjectName("show")
        self.MDlink = QtWidgets.QLabel(self.centralwidget)
        self.MDlink.setGeometry(QtCore.QRect(10, 730, 171, 21))
        self.MDlink.setObjectName("MDlink")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(130, 520, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet("QPushButton{opacity:20%;}")
        self.refresh.setObjectName("refresh")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime Notification"))
        self.add.setText(_translate("MainWindow", "Add Show"))
        self.show.setText(_translate("MainWindow", "List Shows"))
        self.MDlink.setText(_translate("MainWindow", "Made by MD"))
        self.refresh.setText(_translate("MainWindow", "Refresh Keywords"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

