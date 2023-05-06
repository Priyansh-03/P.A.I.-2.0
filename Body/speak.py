#Windows based
# import pyttsx3

# def speak(text):

#     engine = pyttsx3.init("sapi5")
#     voices =engine.getProperty('voices')
#     engine.setProperty('voices',voices[1].id)
#     engine.setProperty('rate',170)
#     # print(f"\n{text}")
#     engine.say(text)
#     engine.runAndWait()

import pai_window
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('Indian English / Aditi')#British English / Brian

def speak(text):
    pai_window.ChatBot.addAppMsg(text)
    

    try:
        lengthoftext = len(str(text))
        if lengthoftext == 0:
            pass
        else:
            print("")
            print(f"PAI : {text}.")
            print("")
            Data = str(text)
            xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
            driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
            driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]')\
                .click()
            driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/form/textarea")\
                .clear()
            if lengthoftext>=30:
                sleep(4)

            elif lengthoftext>=40:
                sleep(6)

            elif lengthoftext>=55:
                sleep(8)

            elif lengthoftext>=70:
                sleep(10)

            elif lengthoftext>=100:
                sleep(13)

            elif lengthoftext>=120:
                sleep(14)

            else:
                sleep(2)
            
    except Exception as e:
        print(f"An error occurred while processing the text, try after some time")
        print("\n\ntrying windows voice voice...")

        import pyttsx3

        engine = pyttsx3.init("sapi5")
        voices =engine.getProperty('voices')
        engine.setProperty('voices',voices[1].id)
        engine.setProperty('rate',170)
        # print(f"\n{text}")
        engine.say(text)
        engine.runAndWait()


