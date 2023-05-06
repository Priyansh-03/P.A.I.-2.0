import datetime
import subprocess
from time import sleep
from datetime import date
import webbrowser
today = date.today()
from Features.wishMe import wish
# from Brain.Commands import specific_commands


# Specify the path to the FxSound file
FxSound = r"C:\Program Files\FxSound LLC\FxSound\FxSound.exe"

# Check if FxSound process is running or not
try:
    output = subprocess.check_output('tasklist', shell=True)
    if 'FxSound.exe' not in str(output):
        # Run the FxSound file using subprocess
        subprocess.Popen(FxSound)
        sleep(2)
except Exception as e:
    print("Error:", e)
    pass

# Specify the path to the VBS file
# vbs_file = r"C:\Users\priya\Desktop\Project-AI(PAI)\welcome greet.vbs"

# # Run the VBS file using subprocess
# try:
#     subprocess.call(['cscript.exe', '//nologo', vbs_file])
# except Exception as e:
#     print("Error:", e)
#     pass

# import pyttsx3
from Body.speak import speak
from Brain.AiBrain import replyBrain
from Brain.QnA import questionAnswer 
from Body.listen import micExecution

# print(">> Starting your P.A.I ! just few seconds.")
# speak(">> Starting your P.A.I ! just few seconds.")

from Features.clap import Tester
from Main import main_task_execution
from PyQt5.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)
import threading
from Gui import GUI



def start_main_execution(gui):
    thread = threading.Thread(target=mainExecution, args=(gui,))
    thread.daemon = True
    thread.start()

def mainExecution(gui):
    # Greet the user
    # speak("Hello, Namaste!")
    wish()
    speak("My name is PAI. How may I help you?")
    

    # Keep running while the GUI is visible
    while gui.isVisible():
        
        # Get user input from the microphone
        try:
            
            data = micExecution()
        except:
            continue
        data = str(data).replace(".", "")
        data = data.lower()

        # Process the input based on the user's intentions
        value_Return = main_task_execution(data)
        if value_Return:
            # Do nothing
            pass
        elif len(data) < 3:
            pass
        else:
            try:
       
                # Handle common questions and commands
                commands = [
                    "what is your name",
                    "what is full form of pai",
                    "what is full form of pie",
                    "what is your full form",
                    "your full form",
                    "who created you",
                    "who developed you",
                    "who made you",
                    "turn on the tv",
                    "what is",
                    "where is",
                    "question",
                    "answer",
                    "shutup",
                    "shut up",
                    "sleep",
                    "keep quiet",
                    "be quiet",
                    "quiet",
                    "be silent",
                    "shut down",
                    "shutdown",
                    "sleep",
                    "close",
                    "restart pc",
                    "restart my pc"
                    "restart computer",
                    "restart my computer",
                    "date",
                    "today",
                    "today's",
                    "time",
                    "search"
                    # "restart pai",
                    # "restart pie"
                    
                ]
                if any(command in data for command in commands):
                    if "what is your name" in data:
                        print("My name is PAI")
                        speak("My name is PAI")

                    elif any(command in data for command in ["what is full form of pai","what is the full form of your name", "what is the full form of pie", "what is your full form", "your full form","your full name"]):
                        print("My full form is: Personal Artificial Intelligence or you can also say, Priyansh's Artificial Intelligence")
                        speak("My full form is: Personal Artificial Intelligence or you can also say, Priyansh's Artificial Intelligence")

                    elif any(command in data for command in ["who created you", "who developed you", "who made you"]):
                        print("I was developed by Priyansh.")
                        speak("I was developed by Priyansh.")

                    elif "search" in data:
                        speak('Searching for ' + data.split('search')[1])
                        url = 'https://google.com/search?q=' + data.split('search')[1]
                        try:
                            webbrowser.get().open(url)
                            speak('This is what I found Sir')
                        except:
                            speak('Please check your Internet')

                    elif 'location' in data:
                        speak('Which place are you looking for ?')
                        temp_audio = micExecution()
                        # app.eel.addUserMsg(temp_audio)
                        speak('Locating...')
                        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
                        try:
                            webbrowser.get().open(url)
                            speak('This is what I found Sir')
                        except:
                            speak('Please check your Internet')            


                    elif "turn on the tv" in data:
                        speak("Ok..Turning On The Android TV")

                    elif (("date" in data) and ("today" or "today's" in data)):
                        speak(today.strftime("%B %d, %Y"))

                    elif "time" in data:
                        speak(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

                    elif any(command in data for command in ["exit","close ai","talk to you later","ttyl","close"]):
                        reply = replyBrain("good bye, greet me farewell in diffrent way")
                        speak(reply)
                        sleep(1)
                        exit(0)
                        

                    elif any(command in data for command in ["shutup","shut up","keep quiet","be silent","quiet","sleep"]):
                        reply = replyBrain("say sorry for speaking too much")
                        speak(reply)
                        print(">> P.A.I. is sleeping....")
                        sleep(10)
                        reply = replyBrain("apologise for making me angry")
                        speak(reply)
                        print(">>P.A.I. is back !!")

                    elif any(command in data for command in ["shut down","shutdown"]):
                        reply = replyBrain("i am turning off my pc")
                        speak(reply)
                        sleep(3)
                        import os
                        os.system("shutdown /s /t 2")  # Shutdown the PC after 1 second delay


                    elif any(command in data for command in ["restart pc","restart my pc","restart computer",
                    "restart my computer"]):
                        reply = replyBrain("i am restarting my pc")
                        speak(reply)
                        sleep(3)
                        import os
                        os.system("shutdown /r /t 2")

                    # elif any(command in data for command in ["restart pai","restart pie"]):
                    #     speak("i am restarting PAI")
                    #     sleep(1)
                    #     clapDetect()


                    elif any(command in data for command in ["what is", "where is", "question", "answer"]):
                        reply = questionAnswer(data)
                        speak(reply)


                    
                # Handle other user inputs using AI
                else:
                    if "close" in data or "exit" in data or "bye" in data or "goodbye" in data or "see you later" in data or "talk to you later" in data or "ttyl" in data:
                        reply = replyBrain("good bye")
                        speak(reply)
                        sleep(2)
                        GUI.closeEvent()
                        exit(0)
                    #reply itself
                    elif "what is"or "where is"or "question"or "answer" in data:
                        reply = questionAnswer(data)
                        if reply != None:
                            speak(reply)

                    else:
                        reply = replyBrain(data)
                        speak(reply)
            except Exception as e:
                print(e)
                pass
def clapDetect():
    # Test the microphone and store the result in 'query'
    
    query = Tester()
    
    # If the microphone is working, continue
    if "True-Mic" in query:
        # Print message to indicate clap detection
        print(">> Clap Detected!!")
        # Speak to indicate clap detection
        speak("Clap detected!")
        
        # Create an instance of the GUI
        gui = GUI()
        # Show the GUI
        gui.show()
        
        # Start the main execution loop in a new thread
        threading.Thread(target=mainExecution, args=(gui,)).start()
        
        # Start the event loop for the GUI
        app.exec_()
        
    # If the microphone is not working, do nothing
    else:
        print("Microphone not detected!")

clapDetect()

