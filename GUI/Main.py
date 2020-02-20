from AddWin_Copy import *
from NewRel import *
#pyqt5 , mysql.connector inside 
# from threading import Thread

''' I need 3 processors :
    1- Tests connection non-stop
    2- notification Window
    3- main window to add things'''

''' New strategy: 
    1- the constant connection test thing in another module
    2- if search for notification everything in main won't work == Disconnect
        * if slef.notif = True:
            self.disco_buttons(connects buttons to message boxes !! )
        * else: ...
        *(the loop isn't executed on an other window but on the main window instead but it loses
        all functionalities till you turn down the notification Button !!! (no threads))
        * f it i think i'll use treading anyways :/
    3- the gif window with the setting will always appear till a notification has been found
    else : it shows a timer till next search
    4- i'll use the multiprossess to scrap the web page instead (remember os.cpu_count )'''

class MainWindow(QMainWindow):#this like a dress for a window object
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi()
        
    def setupUi(self):
        
        self.setWindowTitle("Anime Notification")
        self.resize(1143, 760)

        icon_maker(self)#in NEwRel

        self.pixm = QtWidgets.QLabel(self)
        self.pixm.setGeometry(QtCore.QRect(-50, -50, 1201, 821))
        self.pixm.setText("")
        self.pixm.setPixmap(QtGui.QPixmap("Images/5rc649g05kw11.jpg"))

        self.add = QtWidgets.QPushButton(self)
        self.add.setGeometry(QtCore.QRect(130, 120, 251, 141))

        font = QtGui.QFont()
        font.setFamily("Rainbow Bridge Personal Use")
        font.setPointSize(34)
        self.add.setFont(font)

        self.add.setText("Add Show")
        style1="QPushButton{background-image:url(images/button1.png);\
        border-style: outset;border-width: 2px;border-radius=10px;border-color:whitesmoke;padding:4px;}\
        QPushButton:pressed{color:darkred;background-image:url(images/button2.png);}"

        style2="QPushButton{background-image:url(images/button2.png);\
        border-radius=10px;border-width:2px;border-color:whitesmoke;}\
        QPushButton:pressed{color:darkred;background-image:url(images/button1.png);}"

        self.add.setStyleSheet(style1)

        self.shows = QtWidgets.QPushButton(self)#dude self.show is forbiden XD
        self.shows.setGeometry(QtCore.QRect(130, 320, 251, 141))
        self.shows.setFont(font)
        self.shows.setText("List Shows")#creates and table view with : Title | current episode
        #mn be3d 9ad html file kay usi gogoanime api to get the pics :D or wb scrape lmouhim

        self.shows.setStyleSheet(style2)

        self.refresh = QtWidgets.QPushButton(self)
        self.refresh.setGeometry(QtCore.QRect(130, 520, 251, 141))
        self.refresh.setText("Refresh Keywords") # need to make this one work it\'s quite ez
        font.setPointSize(24)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet(style2)

        self.MDlink = QtWidgets.QLabel(self)
        self.MDlink.setGeometry(QtCore.QRect(10, 730, 171, 21))
        self.MDlink.setText("Made by MD")

        self.notif =  QtWidgets.QPushButton(self)
        self.notif.setGeometry(1030,680,60,60)
        self.notif.setStyleSheet('QPushButton{background-image: url("Images/off 50.png");}')#changes when clicked

        self.get_notif = False#infact True + on_off style turns to False (to be changed afterwards)
        self.on_off_style()

        self.add.clicked.connect(self.AddShow)
        self.shows.clicked.connect(self.URList)
        self.refresh.clicked.connect(self.keyref)
        self.notif.clicked.connect(self.notify)

    def on_off_style(self):#i'll make a simple buttons saying turn on / off notification(color changing)
        if self.get_notif:
            self.notif.setStyleSheet('QPushButton{background-image: url("Images/on 50.png");}')#changes when clicked
            
        else:
            self.notif.setStyleSheet('QPushButton{background-image: url("Images/off 50.png");}')#changes when clicked

    def notify(self):
        self.get_notif = not(self.get_notif)
        ''' There's a problem with this sequence: window activities like clicks cannot be done while a class
        function is still running in that case The While loop. But, i think it's possible to fix that using 
        Treading Module or multiproccesing : Problem --> needs to learn about it it may optimize the Gogoscrap
        module aswell !!!
        But for now i'll be using a pop-up window that runs the notification function repeatedly'''
        self.notificationWin = LoopWin()
        # while self.get_notif==True:
        #     try:
        #         notification()

        #         # cooldown = 200#to be added as attribute when i make a setting window
        #         # seconds = 0
        #         self.on_off_style()#so if no show is added : then the re-style won't occur
        #         # while self.get_notif==True and seconds<cooldown:
        #         #     sleep(0.1)
        #         #     seconds +=0.1 #so if we turn it off it takes 1 sec to reperate the change
        #     except base.errors.ProgrammingError:#database not found
        #         #this chunk need to become a function since it's use alot
        #         msg = QMessageBox()
        #         msg.setWindowTitle('Warning')
        #         msg.setText('No Shows added') 
        #         msg.setIcon(QMessageBox.Critical)

        #         icon = QtGui.QIcon()
        #         icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #         msg.setWindowIcon(icon)

        #         hello = msg.exec_()
        #         self.get_notif = False


    def keyref(self):
        try:
            cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')#change user and passwd
            mycursor = cnx.cursor()
            mycursor.execute('Select Keywords From animeinfo')
            myresult = mycursor.fetchall()
            lod = load_screen()
            lod.show()#TEST **
            for keyw in myresult:
                res = 'https://gogoanimes.ai/search.html?keyword={}&id=-1'.format(keyw)
                scrapURLS(res, keyw)
            lod.close()#TEST **
            cnx.close()
            msg = QMessageBox()
            msg.setWindowTitle('Operation')
            msg.setText('Done!') 
            msg.setIcon(QMessageBox.Information)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            hello = msg.exec_()
        except:#1049 (42000): Unknown database
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setText('No Shows added') 
            msg.setIcon(QMessageBox.Critical)
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            hello = msg.exec_()

    def AddShow(self):
        self.AddDialog = AddWin()
        self.AddDialog.show()

    def URList(self):
        try:
            cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')#change user and passwd
            mycursor = cnx.cursor()
            mycursor.execute('Select title,URL From animeinfo')
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
            cnx.close()
        except:#1049 (42000): Unknown database
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setText('No Shows added') 
            msg.setIcon(QMessageBox.Critical)
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            hello = msg.exec_()

def window_manager():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hel = MainWindow()
    hel.show()
    sys.exit(app.exec_())

def load_screen():
    msg = QMessageBox()
    msg.setWindowTitle('loading')
    msg.setText('Please wait') 
    msg.setIcon(QMessageBox.Information)
    
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    hello = msg.exec_()
    return msg

if __name__ == "__main__":
    window_manager()

    #Thread(target=notification_manager).start()

