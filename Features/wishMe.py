# from datetime import date
import datetime

from Body.speak import speak


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
        
    # speak("I am PAI, how may I help you?")