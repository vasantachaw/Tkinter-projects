import os
from tkinter import *
# from functions.socialLinks import facebook,git,yt,twitter
# from functions.method import Speak
from PIL import Image,ImageTk
import mysql.connector as mq
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
   
#----------------------------
def register():
    winlogin.destroy()
    mypath='register.py'
    os.system('"%s"' %mypath)

def Dashboard():
    winlogin.destroy()
    mypath='dashboard.py'
    os.system('"%s"' %mypath) 

def reset():
    winlogin.destroy()
    mypath='reset.py'
    os.system('"%s"' %mypath)

winlogin=Tk()
winlogin.title('_Login')
winlogin.iconbitmap('images/img/ss.ico')
winlogin.geometry('600x360')
winlogin.config(bg='whitesmoke')


def login_user():
    conn=mq.connect(host='localhost',user='root',password='',database='dbsms')
    cur=conn.cursor()
    sql="select*from register where email=%s and passwords=%s"
    val=(get_email.get(),get_pass.get())
    if conn.is_connected():
        cur.execute(sql,val)
        #conn.commit()2314ol8yw45
        result=cur.fetchall()
        if result:
            Speak('Successfully login and welcome')
            Dashboard()
        else:
            Speak('Invalid password and email id please try again')
            reset()
    else:
        Speak('connection failed')


#--------------------Social Link-----------------------
#https://github.com/Chawbasanta
#https://www.facebook.com/basantaChaw
#https://www.linkedin.com/in/basanta-chaw-15327a201/
#https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA
#https://twitter.com/Ibasanta69

def get_time():
    import time
    timevar=time.strftime("%I:%M:%S  %p")
    clock.config(text=timevar)
    clock.after(200,get_time)





#--------------------Intial-------------------

def reset():
    winlogin.destroy()
    mypath1='search.py'
    os.system('"%s"' %mypath1)
    


#-----------------------------------------------

#----------------------IMage Show part------------------
sideimage=Image.open('images/img/mg.jpg')
sideimage=sideimage.resize((300,370))
sideimg=ImageTk.PhotoImage(sideimage)
sidelabel=Label(winlogin,image=sideimg).place(x=0,y=0)
adminimage=Image.open('images/img/admin.png',)
adminimage=adminimage.resize((100,105))
admin=ImageTk.PhotoImage(adminimage)
adminlabel=Label(winlogin,image=admin).place(x=415,y=20)

#------------------------------------------------------------


#--------------------Button Show Part--------------------------

registerButton=Button(winlogin,text='REGISTER',relief=GROOVE,height=1,width=18,bd=0,command=register)
registerButton.place(x=222,y=290)
resetButton=Button(winlogin,text='RESET PASSWORD',relief=GROOVE,command=reset,height=1,width=18,bd=0)
resetButton.place(x=222,y=310)
clock=Label(winlogin,width=12,height=1,font=('Helavatic',15),fg='#1f1f1f')
clock.place(x=150,y=150)
get_time()
#-----------------------------------------------------------------------

#--------------------------------Social icons ----------------------------------
# ------------------Faceboook------------
facebookimg=Image.open('images/socialIcons/fb.png')
facebookimg=facebookimg.resize((30,30))
facebookimgp=ImageTk.PhotoImage(facebookimg)
facebookbtn=Button(winlogin,image=facebookimgp,bd=0,command=facebook)
facebookbtn.place(x=10,y=300)

#-------------------Twitter------------------
twitterimg=Image.open('images/socialIcons/tw.png')
twitterimg=twitterimg.resize((28,28))
twitterimgp=ImageTk.PhotoImage(twitterimg)
twitterbtn=Button(winlogin,image=twitterimgp,bd=0,command=twitter)
twitterbtn.place(x=50,y=300)

#----------------------Github------------------------------
gitimg=Image.open('images/socialIcons/git.png')
gitimg=gitimg.resize((30,30))
gitimgp=ImageTk.PhotoImage(gitimg)
gitbtn=Button(winlogin,image=gitimgp,bd=0,command=git)
gitbtn.place(x=90,y=300)



#-----------------------Youtube----------------------
ytimg=Image.open('images/socialIcons/yt.png')
ytimg=ytimg.resize((30,30))
ytimgp=ImageTk.PhotoImage(ytimg)
ytbtn=Button(winlogin,image=ytimgp,bd=0,command=yt)
ytbtn.place(x=140,y=300)

#--------------------------------------------------------------------------


#---------------------------------Label Shoiw Part--------------------------
student=Label(winlogin,text='!! S T u d e n t !!')
student.place(x=430,y=140)
get_email=StringVar()
get_pass=StringVar()
userlabel=Label(winlogin,text='E M a i l')
userlabel.place(x=340,y=180)
user=Entry(winlogin,width=25,textvariable=get_email,bg='whitesmoke').place(x=400,y=180)
passlabel=Label(winlogin,text='P A s s',)
passlabel.place(x=340,y=230)
password=Entry(winlogin,width=25,show='*',textvariable=get_pass,bg='whitesmoke')
password.place(x=400,y=230)
signUp=Button(winlogin,text='S I n g I n',relief=GROOVE,command=login_user,bg='lightgray')
signUp.place(x=445,y=270)


#-----------------------Footer Part Show -----------------------
bottom=Frame(winlogin,bg='#59547a',height=20,width=300)
bottom.pack(side=BOTTOM,fill=X)

license=Label(winlogin,text='@Copyright 2023',bg='#59547a',fg='white')
license.place(x=0,y=340)
dev=Label(winlogin,text='@Developed by Chaw basanta',bg='#59547a',fg='white')
dev.place(x=400,y=340)
#--------------------------------------------------------------
winlogin.resizable(False,False)
#WishMe()
#Speak('hi')
#WishMe()
winlogin.mainloop()
