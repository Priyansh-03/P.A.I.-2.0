# import os
import keyboard
import pyautogui
import webbrowser

from time import sleep

from Body.speak import speak

def openExe(query):
    query=str(query).lower()

    if "visit"  in query:
        name_of_web=query.replace("visit","")
        link = f"https://www.{name_of_web}.com"
        speak("searching for your {name_of_web}")
        webbrowser.open(link)
        return True

    elif "launch"  in query:
        name_of_web=query.replace("launch","")
        link = f"https://www.{name_of_web}.com"
        speak(f"launching {name_of_web}")
        webbrowser.open(link)
        return True

    elif "open" in query:
        name_of_app=query.replace("open","")
        speak(f"opening for your {name_of_app}")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(name_of_app)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in query:
        name_of_app=query.replace("open","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(name_of_app)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    
    
