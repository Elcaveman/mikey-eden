# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notificationWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QLabel,QPushButton

class notifWin(QDialog):
    def __init__(self,List):
        super().__init__()
        self.page = 0#default page
        self.List = List
        self.setupUi(0,self.List)
        self.setTitle(0,self.List)
        self.setURL(0,self.List)

    def setupUi(self,page,List):
        self.setWindowTitle('Notification')
        self.resize(737, 492)

        self.BGR = QLabel(self)
        self.BGR.setGeometry(QtCore.QRect(-40, 0, 801, 821))
        self.BGR.setText("")
        self.BGR.setPixmap(QtGui.QPixmap("Images/011.jpg"))#need a better BG

        self.head = QLabel(self)
        self.head.setGeometry(QtCore.QRect(214, 30, 361, 61))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(26)
        self.head.setFont(font)

        self.title1 = QLabel(self)
        self.title1.setGeometry(QtCore.QRect(20, 120, 451, 61))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title1.setFont(font)


        self.watch1 = QPushButton(self)
        self.watch1.setGeometry(QtCore.QRect(490, 140, 93, 28))

        self.seen1 = QPushButton(self)
        self.seen1.setGeometry(QtCore.QRect(610, 140, 93, 28))


        self.seen2 = QtWidgets.QPushButton(self)
        self.seen2.setGeometry(QtCore.QRect(610, 210, 93, 28))

        self.title2 = QtWidgets.QLabel(self)
        self.title2.setGeometry(QtCore.QRect(20, 190, 441, 61))
        self.title2.setFont(font)


        self.watch2 = QPushButton(self)
        self.watch2.setGeometry(QtCore.QRect(490, 210, 93, 28))


        self.seen3 = QPushButton(self)
        self.seen3.setGeometry(QtCore.QRect(610, 280, 93, 28))


        self.watch3 = QPushButton(self)
        self.watch3.setGeometry(QtCore.QRect(490, 280, 93, 28))


        self.title3 = QLabel(self)
        self.title3.setGeometry(QtCore.QRect(20, 260, 441, 61))
        self.title3.setFont(font)


        self.seen4 = QPushButton(self)
        self.seen4.setGeometry(QtCore.QRect(610, 350, 93, 28))


        self.watch4 = QPushButton(self)
        self.watch4.setGeometry(QtCore.QRect(490, 350, 93, 28))


        self.title4 = QLabel(self)
        self.title4.setGeometry(QtCore.QRect(20, 330, 441, 61))
        self.title4.setFont(font)


        self.next = QPushButton(self)
        self.next.setGeometry(QtCore.QRect(630, 430, 81, 28))


        self.back = QPushButton(self)
        self.back.setGeometry(QtCore.QRect(520, 430, 91, 28))

        self.head.setText( "NEW RELEASES!")
        self.watch1.setText( "Watch")
        self.seen1.setText( "Seen")
        self.seen2.setText("Seen")
        self.watch2.setText( "Watch")
        self.seen3.setText( "Seen")
        self.watch3.setText( "Watch")
        self.seen4.setText( "Seen")
        self.watch4.setText( "Watch")
        self.next.setText( "Next ")
        self.back.setText( "Previous")

        #hide buttons in both cases
        if self.page==0:
            self.back.setVisible(False)
        if self.page==len(self.List)-1:
            self.next.setVisible(False)
        
        self.back.clicked.connect(self.backward)
        self.next.clicked.connect(self.forward)
    def backward(self):
        self.page -=1
        self.setTitle(self.page,self.List)
        self.setURL(self.page,self.List)

    def forward(self):
        self.page +=1
        self.setTitle(self.page,self.List)
        self.setURL(self.page,self.List)

    def setTitle(self,page,List):#list = [ inside==page0] // inside = [(title1,URL1)...,(t4,u4)]
        inside = List[page]#count from 0
        
        self.title1.setText(inside[0][0])
        self.title2.setText(inside[1][0])
        self.title3.setText(inside[2][0])
        self.title4.setText(inside[3][0])

    def setURL(self,page,list):#the URL to last_seen_ep+1
        inside = List[page]#count from 0
        
        URL1 = inside[0][1]
        URL2 = inside[1][1]
        URL3 = inside[2][1]
        URL4 = inside[3][1]
        #1
        try:
            self.watch1.disconnect()
        except TypeError:
            pass 
        self.watch1.clicked.connect(browse(URL1))
        #2
        try:
            self.watch2.disconnect()
        except TypeError:
            pass 
        
        self.watch2.clicked.connect(browse(URL2))
        #3
        try:
            self.watch3.disconnect()
        except TypeError:
            pass 
        self.watch3.clicked.connect(browse(URL3))
        #4
        try:
            self.watch4.disconnect()
        except TypeError:
            pass 
        self.watch4.clicked.connect(browse(URL4))

        def browse(URL):#actually tricky u make a function that makes a function
            #that requires no input and that's how u button :D
            def bow():
                from os import startfile
                startfile(URL)
                del startfile
            return bow

