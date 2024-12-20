
from tkinter import *
import os
from PIL import Image, ImageTk
# from functions.method import Speak
# from functions.socialLinks import facebook,git,yt,twitter
import mysql.connector as mq
import pyttsx3 as pt
def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()
     
import webbrowser
def facebook(self):
    webbrowser.open('https://www.facebook.com/basantaChaw')

def git(self):
    webbrowser.open('https://github.com/Chawbasanta')

def twitter(self):
    webbrowser.open('https://twitter.com/Ibasanta69')

def yt(self):
    webbrowser.open('https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA')
   
def Update_pass():
    conn = mq.connect(host='localhost', user='root',
                      password='', database='dbsms')
    cur = conn.cursor()
    sql = "select*from register where email=%s"
    val = [emailid.get()]
    if conn.is_connected():
        cur.execute(sql, val)
        # conn.commit()2314ol8yw45
        result = cur.fetchall()
        if result:
            sqls = 'update register set passswords=%s,conf_passwords=%s where email=%s'
            vals = (password.get(), repassword.get())
            if password.get() == repassword.get():
                if(conn.is_connected()):
                    cur.execute(sqls, vals)
                    conn.commit()
                    Speak('Successfully update your password')
                else:
                    Speak('Unsuccessfully update your password')

            else:
                Speak('Invalid password and email id please try again')
                pass
    else:
        Speak('connection failed')


def get_time():
    import time
    timevar = time.strftime("%I:%M:%S  %p")
    clock.config(text=timevar)
    clock.after(200, get_time)


def back():
    winsearch.destroy()
    mypath1 = 'search.py'
    os.system('"%s"' % mypath1)


def updateLogin():
    winsearch.destroy()
    mypath1 = 'login.py'
    os.system('"%s"' % mypath1)

winsearch = Tk()
winsearch.title('_Search Email')
winsearch.iconbitmap('images/img/ss.ico')
winsearch.geometry('450x260')
winsearch.config(bg='whitesmoke')
winsearch.resizable(False, False)
img = Image.open('images/img/sear.jpg')
img = img.resize((200, 350))
sideimg = ImageTk.PhotoImage(img)
sideimglb = Label(winsearch, image=sideimg)
sideimglb.pack(side=LEFT)
emaillb2 = Label(winsearch, text='E m a i l   I d', font=(
    'Helavatic', 8, 'bold'), fg='black')
emaillb2.place(x=250, y=35)
emaillb1 = Label(winsearch, text='P a s s', font=(
    'Helavatic', 8, 'bold'), fg='black')
emaillb1.place(x=250, y=85)
emaillb = Label(winsearch, text='C o n f  p a s s',
                font=('Helavatic', 8, 'bold'), fg='black')
emaillb.place(x=250, y=135)

search = Label(winsearch, text='R e s e t ', font=(
    'Helavatic', 15, 'bold'), fg='#5dc0cd')
search.place(x=250, y=5)
emailid = StringVar()
password = StringVar()
repassword = StringVar()

email = Entry(winsearch, textvariable=emailid, width=25)
email.place(x=253, y=60)
resetpass = Entry(winsearch, textvariable=password, width=25,show='*')
resetpass.place(x=253, y=110)
reset_conf_pass = Entry(winsearch, textvariable=repassword, width=25,show='*')
reset_conf_pass.place(x=253, y=160)
clock = Label(winsearch, width=12, height=1,
              font=('Helavatic', 15), fg='#1f1f1f')
clock.place(x=50, y=100)
get_time()
# -----------
searchbutton = Button(winsearch, text='U p d a t e', font=(
    'Helavatic', 11), fg='#1f1f1f', relief=GROOVE, width=8,command=Update_pass)
searchbutton.place(x=337, y=190)

backbutton = Button(winsearch, text='B a c k', font=(
    'Helavatic', 11), fg='#1f1f1f', command=back, relief=GROOVE, width=8)
backbutton.place(x=250, y=190)

facebookimg = Image.open('images/socialIcons/fb.png')
facebookimg = facebookimg.resize((27, 27))
facebookimgp = ImageTk.PhotoImage(facebookimg)
facebookbtn = Button(winsearch, image=facebookimgp, bd=0, command=facebook)
facebookbtn.place(x=250, y=225)

# -------------------Twitter------------------
twitterimg = Image.open('images/socialIcons/tw.png')
twitterimg = twitterimg.resize((25, 25))
twitterimgp = ImageTk.PhotoImage(twitterimg)
twitterbtn = Button(winsearch, image=twitterimgp, bd=0, command=twitter)
twitterbtn.place(x=300, y=225)

# ----------------------Github------------------------------
gitimg = Image.open('images/socialIcons/git.png')
gitimg = gitimg.resize((27, 27))
gitimgp = ImageTk.PhotoImage(gitimg)
gitbtn = Button(winsearch, image=gitimgp, bd=0, command=git)
gitbtn.place(x=350, y=225)


# -----------------------Youtube----------------------
ytimg = Image.open('images/socialIcons/yt.png')
ytimg = ytimg.resize((27, 27))
ytimgp = ImageTk.PhotoImage(ytimg)
ytbtn = Button(winsearch, image=ytimgp, bd=0, command=yt)
ytbtn.place(x=400, y=225)

# --------------------------------------------------------------------------


ms = Label(winsearch, text='S T U D E N T   M S')
ms.place(x=50, y=77)

bottom = Frame(winsearch, bg='#207FB7', height=5)
bottom.pack(side=BOTTOM, fill=X)
winsearch.mainloop()
