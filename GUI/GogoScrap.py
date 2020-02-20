from bs4 import BeautifulSoup
import requests
import mysql.connector as base
#UT Done <3
#using GOGOanime site <333

def GetText(list_):
    save=[]
    for tag in list_:
        save.append(tag.text)
    return save

def run_sql_file(filename, connection):
    '''
    The function takes a filename and a connection as input
    and will run the SQL query on the connection  
    '''
    file = open(filename, 'r')
    sql =" ".join(file.readlines())
    cursor = connection.cursor()
    cursor.execute(sql)  
    connection.commit()

def ScrapURL(URL,keyword=None,check=False):#check means u use the function just for checking
    #gets status and saves the last released episode
    #else you do a full search on the show and commits to database if Ongoing
    source = requests.get(URL)
    soup = BeautifulSoup(source.text,"lxml")
    def getTitle():
        div = soup.find('div',class_='anime_info_body_bg')
        h1 = div.find('h1')
        return h1.text
    def getstate():
        div = soup.find('div',class_='anime_info_body_bg')
        p = div.find_all('p')[5] #6th tag is for status
        status = p.text
        if status == "Status: Ongoing":
            return True
        return False
    def getcurent():
        ul = soup.find('ul',{'id':"episode_page"})
        li = ul.find_all('li')[-1]#the last one (works on len==1)
        tx = li.a.text#first is last rel
        if "-" in tx:
            ep = int(tx.split('-')[1])#900-956 for example
        else:
            ep=int(tx)#like the case of: /fategrand-order-zettai-majuu-sensen-babylonia
        #sub = a.find('div',class_='cate').text #get's if it's subed or dubed
        return ep

    tup =status , ep , Title, Url = getstate(), getcurent(),getTitle(),URL
    #opens database and writes into it :D
    if check == False:
        if keyword==None:
            keyword=Title
        if status:
            try:
                cnx = base.connect(host="localhost",user="root",passwd="123010203.*",database='Anime')
                cursor = cnx.cursor()
                cursor.execute('INSERT INTO animeinfo(URL,title,keyword,episode) VALUES(\'{}\',\'{}\',\'{}\', {});'.format(Url,Title,keyword,ep))
                #don't forget the \' for char types
                cnx.commit()
                cnx.close()
            except:
                print('URL already exists')
    if check== True:
        return tup

def scrapURLS(results,keyword):#results is the result of a keyword search
    #URL = 'https://gogoanimes.ai/search.html?keyword={}&id=-1' is the way to go
    #keywords in the database are saved such as you can directly search for them
    Page = 1
    while True:
        URL = results+"&page={}".format(Page) 
        source = requests.get(URL)

        #"BeautifulSoup requires the returned content, not the complete response."

        soup = BeautifulSoup(source.text,"lxml")
        ul = soup.find('div',class_='last_episodes').ul #this is identified as a <class 'bs4.element.Tag'>

        counter = 0
        for li in ul.find_all('li'):
            counter = 1
            div = li.div#the first div is the one i need
            Show  = div.a['href']#the category part of the URL!
            Title = div.a['title']
            URLShow = 'https://www9.gogoanime.io'+Show
            ScrapURL(URLShow,keyword)
        if counter ==0:
            break #means no li left aka this page is empty
        else:    
            Page += 1