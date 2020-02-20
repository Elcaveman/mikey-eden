# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notificationWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import mysql.connector as base
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QLabel,QPushButton,QMessageBox,QMainWindow

class notifWin(QDialog):
    def __init__(self,List):
        super().__init__()
        self.page = 0#default page
        self.List = List
        self.setupUi(self.page,self.List)
        self.setTitle(self.page,self.List)
        self.setURL(self.page,self.List)
       
    def setupUi(self,page,List):
        self.setWindowTitle('Notification')
        self.resize(737, 492)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

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
        for i in range(4):
            watch = getattr(self,'watch{}'.format(i+1))
            seen = getattr(self,'seen{}'.format(i+1))

            watch.setText("Watch")
            watch.setVisible(False)
            

            seen.setText("Seen")
            seen.setVisible(False)

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
        inside = List[page]#count from 0 might not be 4 tho
        for i in range(len(inside)):
            getattr(self,"title{}".format(i+1)).setText(inside[i][0])
            getattr(self,'watch{}'.format(i+1)).setVisible(True)           
            getattr(self,'seen{}'.format(i+1)).setVisible(True)

    def setURL(self,page,List):#the URL to last_seen_ep+1
        inside = List[page]#count from 0

        
        def method(button,function,*args):
            try:
                button.disconnect()
            except TypeError:
                pass 
            button.clicked.connect(function(*args))

        def browse(URL):#actually tricky u make a function that makes a function
            #that requires no input and that's how yu button :D
            def bow():
                from os import startfile
                startfile(URL)
                del startfile
            return bow

        def set_seen(title,ep):
            def saw():
                cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')
                curs = cnx.cursor()
                curs.execute('SELECT id,episode FROM animeinfo WHERE title={}'.format(title))
                Id , ep_base = curs.fetchone()
                if ep == ep_base:
                    msg = QMessageBox()
                    msg.setWindowTitle('Warning')
                    msg.setText('Already Done!!') 
                    msg.setIcon(QMessageBox.Information)

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg.setWindowIcon(icon)
                    hello = msg.exec_()
                else:
                   
                    curs.execute('UPDATE animeinfo SET episode = {} WHERE id = {}'.format(ep,Id))#alter table where id = result(check if tuple) episode = ep and commit <3
                    curs.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle('Information')
                    msg.setText('Operation Done!') 
                    msg.setIcon(QMessageBox.Information)

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg.setWindowIcon(icon)
                    
            return saw

        for i in range(len(inside)):
            #set the watch buttons
            button = getattr(self,"watch{}".format(i+1))
            URL = inside[i][1]
            method(button,browse,URL)
            #set the seen buttons
            button = getattr(self,"seen{}".format(i+1))
            title = inside[i][0]
            ep = inside[i][2]
            method(button,set_seen,title,ep)

    def set_seen(self):
        cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')
        for inside in self.List:
            for tup in inside:
                title = tup[0]
                ep = int(tup[2])
                curs = cnx.cursor()
                curs.execute('SELECT id FROM animeinfo WHERE title={}'.format(title))
                res = curs.fetchone()#id
                curs.execute('')#alter table where id = result(check if tuple) episode = ep and commit <3
                
    