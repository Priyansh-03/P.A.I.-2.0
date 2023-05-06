import speech_recognition as sr
import os



def listen():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)#Listening Mode

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en")

    except:
        return "Error in listening"
    
    query=str(query).lower()
    print(query)
    return query

def wakeUpDetected():
    query=listen().lower()
    # from Body.speak import speak
    if "wake up" in query:
        print(">> Woken Up !! : Starting PAI\n")
        print("\n")
        # speak("Woken up!")
        os.startfile(r'C:\Users\priya\Desktop\Project-AI(PAI)\Ai.py')
    else:
        pass

while True:
    wakeUpDetected()
    print("\n")