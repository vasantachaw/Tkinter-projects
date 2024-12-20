import os
from tkinter import X, Y
from tkinter import*
from tkinter import font
from tkinter import messagebox
from tkinter.font import BOLD, families
from typing import Sized
from PIL import ImageTk, Image
import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


class pc():
    def shutdown():
        speak("Your computer will be shuttdown in 30 seconds")
        os.system('shutdown -s -t 30')

    def restart():
        speak("Your computer restarting now !")
        os.system('shutdown/r')

    def logoff():
        speak("Your computer loggoff now !")
        os.system('shutdown/l')

    def sleep():
        speak("your computer sleep now !")
        os.system('shutdown/h')

    def abort():
        speak("your  computer abort !")
        os.system('shutdown/a')


class shuttdownForm():
    def Formm():
        shutform = Tk()
        shutform.title("Power Button")
        shutform.iconbitmap("C:\\Users\\Death Empire\\Downloads\\h.ico")
        shutform.geometry("300x100")
        lb = Label(shutform, text="Power Buttons").place(x=200, y=40)
        but1 = Button(shutform, text="Shutdown", fg="green",
                      command=pc.shutdown).place(x=70, y=11)
        but2 = Button(shutform, text="Restart", fg="red",
                      command=pc.restart).place(x=80, y=50)
        but3 = Button(shutform, text="Sleep", fg="purple",
                      command=pc.sleep).place(x=140, y=50)
        but4 = Button(shutform, text="Cancell", fg="brown",
                      command=pc.abort).place(x=20, y=50)
        shutform.resizable(False, False)


def login():
    user = input.get()
    pas = input1.get()
    if user == 'admin' and pas == 'admin':
        speak("Welcome Welcome")
        shuttdownForm.Formm()
    else:
        speak("Sorry invalid your password and Username !")
        ms = messagebox.showerror("Wrong", "Invalid pass & User !")


speak('goood morning sir')
window = Tk()
window.title("Login")
window.geometry("350x300")
window.config(bg="pink")

fram = Frame(window).pack(fill=BOTH, expand=True)
window.iconbitmap("C:\\Users\\Death Empire\\Downloads\\h.ico")
loginimg = PhotoImage(file="C:\\Users\\Death Empire\\Downloads\\11.png")

# Create Simple Login Box In Python

admin = Label(window, image=loginimg,
              border=0, height=100, width=80).place(x=133, y=10)
label = Label(window, text="username", fg="black",
              font=BOLD, border=0).place(x=25, y=120)
input = Entry(window, width=15, font=BOLD,
              fg="black", border=0, justify=CENTER)
input.place(x=105, y=120)
label1 = Label(window, text="password", fg="black",
               font=BOLD, border=0,).place(x=25, y=160)
input1 = Entry(window, width=15, font=BOLD, fg="black",
               border=0, justify=CENTER, show="*")
input1.place(x=105, y=160)
Button2 = Button(window, text="Sumbit", font=BOLD,
                 fg="green", bd=0.5, command=login,relief="groove").place(x=105, y=200)
Button1 = Button(window, text="Exit", font=BOLD, fg="red",relief=GROOVE,
                 command=window.quit, bd=0.5, width=6).place(x=180, y=200)
lab = Label(window, text="@basanta chaudhary").place(x=115, y=250)
window.resizable(FALSE, FALSE)
window.mainloop()
