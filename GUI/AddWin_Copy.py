from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from GogoScrap import *
from time import sleep

def makedb():
    import mysql.connector as base
    try:
        cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')#change user and passwd
    except base.errors.ProgrammingError:#1049 (42000): Unknown database
        cnx = base.connect(host="localhost",user="root",passwd="123010203.*")
        #we create the database the sql file is in Data folder
        run_sql_file('Data/init database.sql',cnx)
        cnx.close()
        cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')
        run_sql_file('Data/init table.sql',cnx)
        cnx.close()

def caps(text):
    list_=text.split(' ')
    new=""
    for i in range(len(list_)):
        elt = list_[i]
        new = new + elt.capitalize()
        if i!=len(list_)-1:
            new = new + '+'#+ instead of ' ' for the site keyword search
    return new    

class AddWin(QDialog):
    def __init__(self):
        makedb()
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Add proto 1.0")
        self.setGeometry(50,30,843, 271)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
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

    def accept(self):#overwriting the original
        from os import startfile
        bool_=self.RadioUrl.isChecked()
        if bool_:
            URL = self.Name.text()
            ok = 'URL'
        else:
            name = caps(self.Name.text())
            URL = 'https://gogoanimes.ai/search.html?keyword={}&id=-1'.format(name)
            ok = 'keyword'
        Title='Verification'
        Text='Do you want to check this {}?'.format(ok)
        buttonReply = QMessageBox.question(self,Title,Text, QMessageBox.Yes | QMessageBox.No)
        #buttonReply actually blocks the passage of things
        if buttonReply == QMessageBox.Yes:
           startfile(URL)
        #this happens once you click OK
        buttonReply = QMessageBox.question(self,Title,'The {} will be added are you sure?'.format(ok), QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if bool_:
                ScrapURL(URL)
            else:
                scrapURLS(URL,keyword=name)#Hello get all the anime urls//current episodes
            msg = QMessageBox()
            msg.setWindowTitle('Operation')
            msg.setText('Done!') 
            msg.setIcon(QMessageBox.Information)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            hello = msg.exec_()
            self.close()