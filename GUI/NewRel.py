import time
#import timestring the problem is the objects are not from the same class :/
from notificationWin import *
from GogoScrap import *
import sys

def icon_maker(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

def notification():
        List = []
        '''proccess1'''
        cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')
        cursor = cnx.cursor()
        cursor.execute('SELECT URL,title,episode FROM animeinfo;')
        result =cursor.fetchone()#tuple

        tx = "New realeses have been found do you wanna see?"
        flag = 0
        inside = []
        while result!= None:
                Url_ , title_ , ep_ = result
                status , ep , *_ = ScrapURL(Url_,keyword=None,check=True)#keyword is not important we'll use an URL by URL check
                if ep_ < ep:
                        if flag ==0:
                                app = QtWidgets.QApplication(sys.argv)
                                useless = QMainWindow()
                                buttonReply = QMessageBox.question(None,"Notification",tx, QMessageBox.Yes | QMessageBox.No)
                                if buttonReply == QMessageBox.Yes:
                                        useless.close()
                                        flag = 1 #means let's continue the search
                                        #https://www9.gogoanime.io/kimetsu-no-yaiba-episode-23
                                        #https://www9.gogoanime.io/category/kimetsu-no-yaiba
                                        URL_New = ''.join(Url_.split('category/'))+'-episode-'+str(ep_+1)
                                        inside.append((title_,URL_New,ep))#ep = last realeased episode
                                else:
                                        cnx.close()
                                        return False#breaks the function

                        else:
                                URL_New = ''.join(Url_.split('category/'))+'-episode-'+str(ep+1)
                                inside.append((title_,URL_New))

                result = cursor.fetchone()
                if len(inside) == 4 or result==None:
                        List.append(inside)#set page numbr x
                        inside = []
                
        return List

class LoopWin(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi()
                self.show()
        def setupUi(self):
                self.setWindowTitle('Searching for notification')
                self.setGeometry(50,50,450, 150)
                
                icon_maker(self)
                self.label = QLabel(self)
                self.label.setGeometry(QtCore.QRect(10, 30, 300, 51))
                font = QtGui.QFont()
                font.setFamily("MS Sans Serif")
                font.setPointSize(15)
                self.label.setFont(font)
                
                #how to gif :D
                
                
                self.Load = QLabel(self)                  
                self.movie = QtGui.QMovie("Images/loading-gif.gif")
                self.Load.setMovie(self.movie)
                self.movie.start()
                self.Load.setGeometry(QtCore.QRect(330, 30, 100, 70))
                self.Load.setScaledContents(True)
                

                self.menubar = QtWidgets.QMenuBar(self)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 26))
                font.setPointSize(10)
                self.menubar.setFont(font)
                self.menusettings = QtWidgets.QMenu(self.menubar)
                self.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(self)

                self.setStatusBar(self.statusbar)

                self.Refresh_frequency = QtWidgets.QAction(self)

                self.Refresh_manualy = QtWidgets.QAction(self)

                self.menusettings.addAction(self.Refresh_frequency)#how to connect them to fcts
                self.menusettings.addAction(self.Refresh_manualy) #how to connect them to fcts
                self.menubar.addAction(self.menusettings.menuAction())


                self.setWindowTitle("Notification Window")
                self.label.setText("Searching for notifications.")
                self.menusettings.setTitle("settings")

                self.Refresh_frequency.setText("Refresh frequency")
                self.Refresh_manualy.setText("Refresh manualy")

                self.Refresh_frequency.setShortcut('CTRL+f')
                self.Refresh_manualy.setShortcut('CTRL+m')
                
                self.Refresh_frequency.triggered.connect(self.freq)
                self.Refresh_manualy.triggered.connect(self.refresh)

        def freq(self):#UT done
                text , ok = QtWidgets.QInputDialog.getText(self,'Get Sleep Time', "Sleep Time:(H:M:S)")
                def clean_form(text):
                        list_ = text.split(':')
                        if 1<=len(list_)<=3:#convert_all to seconds
                                try:
                                        hours = int(list_[0])*3600
                                        mins = int(list_[1])*60
                                        secs = int(list_[2])
                                        summ = secs+mins+hours
                                except IndexError:
                                        try:
                                                mins = int(list_[0])*60
                                                secs = int(list_[1])
                                                summ = secs + mins
                                        except IndexError:
                                                secs = int(list_[0])
                                                summ = secs
                                return summ
                        else:
                                msg = QMessageBox()
                                msg.setWindowTitle('Warning')
                                msg.setText('Wrong format') 
                                msg.setIcon(QMessageBox.Information)

                                icon = QtGui.QIcon()
                                icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                                msg.setWindowIcon(icon)
                                hello = msg.exec_()
                if ok:                   
                        with open('Data/sleep time.txt','w') as f:
                                summ = clean_form(text)
                                if summ != None:
                                        f.write(str(summ))
                                else:
                                        self.freq()
                self.refresh()#this function restarts the notification searching / sleeping proccess
        def refresh(self):
                pass
                #it will exit the current processor sleeping and getting notficitation()+ notifWin
                #and reboots it
                #afterwards we need a tread for the gif so when notifs are sleeping u get a timer: TIME BEFORE NEXT SCRAP
                
if __name__ == "__main__":
    import sys
    #List = notification()
    app = QtWidgets.QApplication(sys.argv)
    '''test 2'''
    win = LoopWin()
    ''' test 1'''
#     win = notifWin(List)
#     win.show()
    sys.exit(app.exec_())
