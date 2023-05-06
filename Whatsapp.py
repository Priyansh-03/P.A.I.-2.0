import pyautogui
import time
from Body.speak import speak
from Body.listen import micExecution
from Features.Open import openExe

def maximize_window():
    # Check if the window is maximized
    if not pyautogui.getWindowsWithTitle("WhatsApp")[0].isMaximized:
        pyautogui.hotkey('win', 'up')

def send_whatsapp_message(contact_name):
    

    # Open the WhatsApp application
    speak("Initializing The Whatsapp Software.")
    # whatsapp_path = "whatsapp"  # Replace with the actual file path if needed
    openExe("open whatsapp")

    # Maximize the WhatsApp window
    maximize_window()
   


    x = 239  # Replace with the x-coordinate of the location
    y = 145  # Replace with the y-coordinate of the location
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(2)

    pyautogui.write(contact_name)
    while True:
        speak(f"Please confirm..do you want to send message to this first contact which appeared?")
        input=micExecution()
        input.lower()
        if  ("yes") in input  or ("correct") in input :
        # Prepare to send a message
            speak(f"Preparing To Send a Message To {contact_name}, please do not touch")
            break
        elif (("no") in input) or (("deny") in input)  or (("change")  in input) or (("no one") in input):
            speak("ok, canceling your request")
            return True
        else:
            speak("canceling your request")
            return True
        
    time.sleep(2)

   # Move the cursor to the specified location and click the mouse after a delay
    x = 218  # Replace with the x-coordinate of the location
    y = 226  # Replace with the y-coordinate of the location
    pyautogui.moveTo(x, y)
    time.sleep(2)  # Wait for 2 seconds
    pyautogui.click()
    # send_whatsapp_message(contact_name)
    time.sleep(2)

    # Ask for the message to send
    speak("What's The Message By The Way?")
    message = micExecution()
    
    pyautogui.write(message)

    # Send the message
    time.sleep(5)
    pyautogui.press('enter')
    speak(f"sent ,{message} to ,{contact_name} sucessfully!")

# if __name__ == '__main__':
#     send_whatsapp_message("rishika psit")



# from time import sleep
# from Body.speak import speak
# from Body.listen import micExecution
# from Features.Open import openExe
# import pyautogui
# import time

# speak("Initializing The Whatsapp Software.")
# whatsapp_path = "whatsapp"

# # Open the WhatsApp application
# pyautogui.press('win')
# time.sleep(1)
# pyautogui.write(whatsapp_path)
# pyautogui.press('enter')
# time.sleep(8)


# pyautogui.hotkey('win', 'up')

# def newLine():
#     pyautogui.keyDown('shift')
#     pyautogui.press('enter')
#     pyautogui.keyUp('shift')


# def WhatsappSender(Name):
#     speak(f"Preparing To Send a Message To {Name}")
#     pyautogui.write(Name)
#     time.sleep(2)

#     # Move the cursor to the specified location and click the mouse after a delay
#     x = 218  # Replace with the x-coordinate of the location
#     y = 226  # Replace with the y-coordinate of the location
#     pyautogui.moveTo(x, y)
#     time.sleep(2)  # Wait for 2 seconds
#     pyautogui.click()
#     time.sleep(2)

#     speak("What's The Message By The Way?")
#     message = micExecution()
#     if "new line" in message:
#         message=message.replace("new line",newLine())
    
#     time.sleep(2)
#     pyautogui.write(message)
#     sleep(10)

#     pyautogui.press('enter')

# WhatsappSender("")