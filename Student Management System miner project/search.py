
from tkinter import *
#from functions.socialLinks import facebook,git,yt,twitter
import os
from PIL import Image,ImageTk
import mysql.connector as mq
#from functions.method import Speak
import webbrowser
import pyttsx3 as pt
def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()
     
def facebook(self):
    webbrowser.open('https://www.facebook.com/basantaChaw')

def git(self):
    webbrowser.open('https://github.com/Chawbasanta')

def twitter(self):
    webbrowser.open('https://twitter.com/Ibasanta69')

def yt(self):
    webbrowser.open('https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA')
   
def get_time():
    import time
    timevar=time.strftime("%I:%M:%S  %p")
    clock.config(text=timevar)
    clock.after(200,get_time)

def back():
    winsearch.destroy()
    mypath1='login.py'
    os.system('"%s"' %mypath1)

def reset():
    winsearch.destroy()
    mypath1='reset.py'
    os.system('"%s"' %mypath1)
 #------------------------------------------------------
def sql_search_email():
    conn=mq.connect(host='localhost',user='root',password='',database='dbsms')
    cur=conn.cursor()
    sql="select*from register where email=%s"
    val=[emailId.get()]
    if conn.is_connected():
        cur.execute(sql,val)
        #conn.commit()2314ol8yw45
        result=cur.fetchall()
        if result:
            Speak('Successfully  and welcome')
            reset()
        else:
            Speak('Invalid  email id please try again')
            pass
    else:
        Speak('connection failed')


winsearch=Tk()
winsearch.title('_Search Email')
winsearch.iconbitmap('images/img/ss.ico')
winsearch.geometry('500x260')
winsearch.config(bg='whitesmoke')
winsearch.resizable(False,False)
img=Image.open('images/img/sear.jpg')
img=img.resize((200,350))
sideimg=ImageTk.PhotoImage(img)
sideimglb=Label(winsearch,image=sideimg)
sideimglb.pack(side=LEFT)

emaillb=Label(winsearch,text='E m a i l   I D',font=('Helavatic',8,'bold'),fg='#81bcc4')
emaillb.place(x=320,y=95)
search=Label(winsearch,text='S e a r c h i n g .  .',font=('Helavatic',15,'bold'),fg='#5dc0cd')
search.place(x=270,y=55)
emailId=StringVar()
email=Entry(winsearch,textvariable=emailId,width=33)
email.place(x=253,y=120)

clock=Label(winsearch,width=12,height=1,font=('Helavatic',15),fg='#1f1f1f')
clock.place(x=50,y=100)
get_time()
#-----------
searchbutton=Button(winsearch,text='S e a r c h',font=('Helavatic',11),fg='#1f1f1f',relief=GROOVE,width=10,command=sql_search_email)
searchbutton.place(x=357,y=170)

backbutton=Button(winsearch,text='B a c k',font=('Helavatic',11),fg='#1f1f1f',command=back,relief=GROOVE,width=10)
backbutton.place(x=255,y=170)

facebookimg=Image.open('images/socialIcons/fb.png')
facebookimg=facebookimg.resize((30,30))
facebookimgp=ImageTk.PhotoImage(facebookimg)
facebookbtn=Button(winsearch,image=facebookimgp,bd=0,command=facebook)
facebookbtn.place(x=260,y=215)

#-------------------Twitter------------------
twitterimg=Image.open('images/socialIcons/tw.png')
twitterimg=twitterimg.resize((28,28))
twitterimgp=ImageTk.PhotoImage(twitterimg)
twitterbtn=Button(winsearch,image=twitterimgp,bd=0,command=twitter)
twitterbtn.place(x=310,y=215)

#----------------------Github------------------------------
gitimg=Image.open('images/socialIcons/git.png')
gitimg=gitimg.resize((30,30))
gitimgp=ImageTk.PhotoImage(gitimg)
gitbtn=Button(winsearch,image=gitimgp,bd=0,command=git)
gitbtn.place(x=360,y=215)



#-----------------------Youtube----------------------
ytimg=Image.open('images/socialIcons/yt.png')
ytimg=ytimg.resize((30,30))
ytimgp=ImageTk.PhotoImage(ytimg)
ytbtn=Button(winsearch,image=ytimgp,bd=0,command=yt)
ytbtn.place(x=420,y=215)

#--------------------------------------------------------------------------


ms=Label(winsearch,text='S T U D E N T   M S')
ms.place(x=50,y=77)

bottom=Frame(winsearch,bg='#207FB7',height=5)
bottom.pack(side=BOTTOM,fill=X)
winsearch.mainloop()