import os
import datetime as dat
from tkinter import X, Y
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.font import BOLD, families
from typing import Sized

from PIL import ImageTk, Image
import pyttsx3
from pyttsx3 import engine

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def Wish_me():
    hour = int(dat.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning !")
    elif hour > 12 and hour <= 17:
        speak("Good Afternoon !")
    elif hour > 17 and hour <= 21:
        speak("Good Evening !")
    else:
        speak("Good Night Have a You Nice Dream !")


class pc:

    def shutdown():
        speak("Your computer will be shuttdown in 30 seconds")
        os.system("shutdown -s -t 30")

    def restart():
        speak("Your computer restarting now !")
        os.system("shutdown/r")

    def logoff():
        speak("Your computer loggoff now !")
        os.system("shutdown/l")

    def sleep():
        speak("your computer sleep now !")
        os.system("shutdown/h")

    def abort():
        speak("your  computer abort !")
        os.system("shutdown/a")


class shuttdownForm:

    def Formm():
        shutform = Tk()
        shutform.title("Power Button")
       #shutform.iconbitmap("C:\\Users\\Death Empire\\Downloads\\h.ico")
        shutform.geometry("300x100")
        lb = Label(shutform, text="Power Buttons").place(x=200, y=40)
        but1 = Button(shutform,
                      text="Shutdown",
                      fg="green",
                      command=pc.shutdown).place(x=70, y=11)
        but2 = Button(shutform, text="Restart", fg="red",
                      command=pc.restart).place(x=80, y=50)
        but3 = Button(shutform, text="Sleep", fg="purple",
                      command=pc.sleep).place(x=140, y=50)
        but4 = Button(shutform, text="Cancell", fg="brown",
                      command=pc.abort).place(x=20, y=50)
        shutform.resizable(False, False)
        shutform.mainloop()


#Wish_me()
shuttdownForm.Formm()
