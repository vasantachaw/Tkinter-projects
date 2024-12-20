from tkinter import *

from PIL import Image, ImageTk
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
   
# from functions.method import Speak
# from functions.socialLinks import facebook,yt,twitter,git
winregist = Tk()
winregist.geometry('700x350')
winregist.iconbitmap('images/img/ss.ico')
winregist.title('_register')
winregist.config(bg='whitesmoke')
imgregist = Image.open('images/img/regist.jpg')
imgregist = imgregist.resize((400, 300))
imgreside = ImageTk.PhotoImage(imgregist)
registlabel = Label(winregist, image=imgreside)
registlabel.pack(side=LEFT)

# ---------------------------Database Connection Part------------------------------------


def mysqlregister():

    conn = mq.connect(host='localhost', user='root',
                           password='', database='dbsms')
    curs = conn.cursor()
    sql = ('insert into register (fname,lname,email,sex,passwords,conf_passwords,address,contact) values(%s,%s,%s,%s,%s,%s,%s,%s)')
    if passwords.get()==confirmpasswords.get():

        if sex.get() == 1:
            male = 'male'
            val = [fnames.get(), lnames.get(), emails.get(), male, passwords.get(
            ), confirmpasswords.get(), addresses.get(), contacts.get()]
       
            if(conn.is_connected()):
                if(conn.is_connected()!=0):
                    curs.execute(sql, val)
                    conn.commit()
                    Speak('Successfully Inserted Data !')
                else:
                    Speak('Unsucessfully Inserted Data !')
            else:
                Speak('Unsuccessfully connection')

        elif sex.get()==0:
            female = 'female'
            vals = [fnames.get(), lnames.get(), emails.get(), female, passwords.get(
            ), confirmpasswords.get(), addresses.get(), contacts.get()]
            if(conn.is_connected()):
                if(conn.is_connected()!=0):
                    curs.execute(sql,vals)
                    conn.commit()
                    Speak('Successfully Inserted Data !')
                else:
                    Speak('Unsucessfully Inserted Data !')
            else:
                Speak('Unsuccessfully connection')
        curs.close()
        conn.close()
    else:
        Speak('Invalid password please try again')
    
      
# --------------------------------------------------------------
def clearEnrty():
    fname.delete(0, END)
    lname.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    confirmpassword.delete(0, END)
    address.delete(0, END)
    contact.delete(0, END)


def get_time():
    import time
    timevar = time.strftime("%I:%M:%S  %p")
    clock.config(text=timevar)
    clock.after(200, get_time)
# https://github.com/Chawbasanta
# https://www.facebook.com/basantaChaw
# https://www.linkedin.com/in/basanta-chaw-15327a201/
# https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA
# https://twitter.com/Ibasanta69


def getdata():
    print(fnames.get())
    print()
    print(lnames.get())
    print()
    print(emails.get())
    print()
    print(addresses.get())
    print()
    print(contacts.get())
    print()
    print(passwords.get())
    print(confirmpasswords.get())
    if sex.get() == 1:
        print('Male')
    else:
        print('Female')


# -------------------------------

# --------------------------------Social icons ----------------------------------
# ------------------Faceboook------------
facebookimg = Image.open('images/socialIcons/fb.png')
facebookimg = facebookimg.resize((20, 20))
facebookimgp = ImageTk.PhotoImage(facebookimg)
facebookbtn = Button(winregist, image=facebookimgp, bd=0, command=facebook)
facebookbtn.place(x=150, y=326)

# -------------------Twitter------------------
twitterimg = Image.open('images/socialIcons/tw.png')
twitterimg = twitterimg.resize((18, 18))
twitterimgp = ImageTk.PhotoImage(twitterimg)
twitterbtn = Button(winregist, image=twitterimgp, bd=0, command=twitter)
twitterbtn.place(x=180, y=326)

# ----------------------Github------------------------------
gitimg = Image.open('images/socialIcons/git.png')
gitimg = gitimg.resize((20, 20))
gitimgp = ImageTk.PhotoImage(gitimg)
gitbtn = Button(winregist, image=gitimgp, bd=0, command=git)
gitbtn.place(x=205, y=326)


# -------------------------Clock----------------
clock = Label(winregist, width=12, height=1, font=(
    'Helavatic', 12, 'bold'), fg='#1f1f1f', bg='whitesmoke')
clock.place(x=150, y=0)
get_time()
# -------------


# -----------------------Youtube----------------------
ytimg = Image.open('images/socialIcons/yt.png')
ytimg = ytimg.resize((20, 20))
ytimgp = ImageTk.PhotoImage(ytimg)
ytbtn = Button(winregist, image=ytimgp, bd=0, command=yt)
ytbtn.place(x=240, y=326)

# -----------------------Footer Part Show -----------------------
bottom = Frame(winregist, bg='#59547a', height=20, width=300)
bottom.pack(side=BOTTOM, fill=X)

# license=Label(bottom,text='@Copyright 2023',bg='#59547a',fg='white')
# license.place(x=0,y=330)
dev = Label(winregist, text='@Developed by Chaw basanta',
            bg='#59547a', fg='white')
dev.place(x=460, y=330)
# --------------------------------------------------------------

# ----------------------Entrybox-0----------------------------
fnames = StringVar()
lnames = StringVar()
sex = IntVar()
emails = StringVar()
passwords = StringVar()
confirmpasswords = StringVar()
addresses = StringVar()
contacts = StringVar()

sms = Label(winregist, text='S T U D E N T    M S',
            font=('Monospace', 15, 'bold'), fg='#75acf0')
sms.place(x=50, y=100)

student = Label(winregist, text='S T U D E N T  R E G I S T E R',
                font=('Helavatic', 13, 'bold'), fg='#75acf0')
student.place(x=50, y=133)
fnamelb = Label(winregist, text='f i r s t     n a m e')
fnamelb.place(x=420, y=45)
fname = Entry(winregist, textvariable=fnames)
fname.place(x=420, y=70)

lnamelb = Label(winregist, text='l a s t     n a m e')
lnamelb.place(x=560, y=45)
lname = Entry(winregist, textvariable=lnames)
lname.place(x=560, y=70)


emaillb = Label(winregist, text='e m a i l   i d')
emaillb.place(x=420, y=105)
email = Entry(winregist, textvariable=emails, width=30)
email.place(x=420, y=130)
# ---------------------Radio button ------------------------------
malelb = Label(winregist, text='male')
malelb.place(x=612, y=105)
male = Radiobutton(winregist, value=1, variable=sex)
male.place(x=620, y=125)

femalelb = Label(winregist, text='female')
femalelb.place(x=650, y=105)
female = Radiobutton(winregist, value=0, variable=sex)
female.place(x=660, y=125)

# -------------------------------------------------------
# ---------------------Passwords field--------------------

passwordlb = Label(winregist, text='p a s s w o r d')
passwordlb.place(x=420, y=160)
password = Entry(winregist, textvariable=passwords, show='*')
password.place(x=420, y=185)

confirmpasswordlb = Label(winregist, text='c o n f   p a s s w o r d')
confirmpasswordlb.place(x=560, y=160)
confirmpassword = Entry(winregist, textvariable=confirmpasswords, show='*')
confirmpassword.place(x=560, y=185)


# ------------------------------------------------------
addresslb = Label(winregist, text='a d d r e s s  ')
addresslb.place(x=420, y=215)
address = Entry(winregist, textvariable=addresses, width=25)
address.place(x=420, y=240)
contactlb = Label(winregist, text='c o n t a c t  ')
contactlb.place(x=590, y=215)
contact = Entry(winregist, width=15, text=contacts)
contact.place(x=590, y=240)
# --------------------------Button---------------------

clearbutton = Button(winregist, text='C l e a r', width=17, relief=GROOVE, font=(
    'Helavatic', 9, 'bold'), bg='#ff7163', command=clearEnrty)
clearbutton.place(x=420, y=280)

submit = Button(winregist, text='S u b m i t', width=17, relief=GROOVE, font=(
    'Helavatic', 9, 'bold'), bg='#6ecb6f', command=mysqlregister)
submit.place(x=560, y=280)

# -----------------------------------------------
footer = Label(winregist, width=15, height=1, text='@Copyright 2023',
               font=('Helavatic', 9), fg='#1f1f1f', bg='#f0b548')
footer.place(x=3, y=327)

winregist.resizable(False, False)
winregist.mainloop()
