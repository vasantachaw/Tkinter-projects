import datetime
import pyttsx3 as pt
def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()
        
def WishMe():
   
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Goood Morning have a you nice today ')
    elif hour >=12 and hour<18:
        Speak('Good Afternoon')
    elif hour>=18 and hour < 20:
        Speak('Good Evening')
    else:
        Speak('Goood night ')
   