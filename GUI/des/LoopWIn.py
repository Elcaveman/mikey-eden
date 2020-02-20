# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoopWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 148)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.load = QtWidgets.QLabel(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(280, 30, 71, 60))
        self.load.setText("")
        self.load.setPixmap(QtGui.QPixmap("../Images/loading-gif.gif"))
        self.load.setScaledContents(True)
        self.load.setObjectName("load")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 26))
        self.menubar.setObjectName("menubar")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh_frequency = QtWidgets.QAction(MainWindow)
        self.actionRefresh_frequency.setObjectName("actionRefresh_frequency")
        self.actionRefresh_manualy = QtWidgets.QAction(MainWindow)
        self.actionRefresh_manualy.setObjectName("actionRefresh_manualy")
        self.menusettings.addAction(self.actionRefresh_frequency)
        self.menusettings.addAction(self.actionRefresh_manualy)
        self.menubar.addAction(self.menusettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notification Window"))
        self.label.setText(_translate("MainWindow", "Searching for notifications."))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))
        self.actionRefresh_frequency.setText(_translate("MainWindow", "Refresh frequency"))
        self.actionRefresh_manualy.setText(_translate("MainWindow", "Refresh manualy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

