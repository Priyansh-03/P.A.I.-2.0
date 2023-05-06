import speech_recognition as sr
from googletrans import Translator
from time import sleep

#Listen

def listen():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)#Listening Mode

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query=str(query).lower()
    return query

#Translation

def translation_to_english(text):
    line=str(text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"You: {data}.")
    return data

# Connecting to mic

def micExecution():
    query=listen()
    data=translation_to_english(query)
    
    return data

