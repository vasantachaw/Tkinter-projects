
import datetime
from tkinter import*
import pyttsx3
from tkinter import Label
from tkinter import filedialog
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
def stopSpeech():
    engine=pyttsx3.init()
    engine.stop()
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning  Basant Chaudhary  !  ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Basant Chaudhary")
    else:
        speak("Good Evening! Basant Chaudhary")


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def text_to_speech():
    st1 = textentry.get("1.0", "end")
    speak(st1)


def clear_text_contents():
    textentry.delete('1.0', 'end')


def openfile():
    myfile = filedialog.askopenfilename(initialfile="")
    filing = open(myfile, 'r')
    # print(filing.read())
    textentry.insert('1.0', filing.read())


def savefile():
    svr = textentry.get('1.0', 'end')
    savefiles = filedialog.asksaveasfile(
        initialfile="untild.txt", title="File save", defaultextension='.txt', mode='w', filetypes=[('TXT', '*.txt')])
    try:
        savefiles.write(svr)
    except:
        print()
        # console hidde

win = Tk()
file = StringVar()
myfile = StringVar()
win.geometry("700x370")
win.config(bg='pink')
win.resizable(False, False)
win.title("ReadMode")
win.iconbitmap('images/img/ss.ico')
textlabel = Label(win, text="Text To Speech",
                  font="Arial 15")
textlabel.place(x=290, y=15)

textentry = Text(win, width=100, height=20)
textentry.place(x=0, y=0)
eft=Frame(win,height=47,bg='pink').pack(side=BOTTOM,fill=X)
Open=Button(win,text='Open',font=('Arial',12,'bold'),fg='gray',bg='pink',width=7,relief=GROOVE,command=openfile).place(x=5,y=330)
save=Button(win,text='Save',font=('Arial',12,'bold'),fg='gray',width=7,bg='pink',relief=GROOVE,command=savefile).place(x=93,y=330)
play=Button(win,text='PLay',font=('Arial',12,'bold'),fg='gray',width=7,bg='pink',relief=GROOVE,command=text_to_speech).place(x=180,y=330)
pause=Button(win,text='Pause',font=('Arial',12,'bold'),fg='gray',width=7,bg='pink',relief=GROOVE).place(x=270,y=330)
clears=Button(win,text='Clear',font=('Arial',12,'bold'),fg='gray',width=7,bg='pink',relief=GROOVE,command=clear_text_contents).place(x=360,y=330)
labels=Label(win,text='Text-To-Speech',font=('Arial',20,'bold'),bg='pink',fg='tomato').place(x=470,y=328)
win.mainloop()
