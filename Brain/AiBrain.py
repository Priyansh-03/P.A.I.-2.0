#Api key
fileopen = open("C:\\Users\\priya\\Desktop\\Project-AI(PAI)\\Data\\api.txt","r")
api=fileopen.read()
fileopen.close()

#importing
import openai
from dotenv import load_dotenv

#coding

openai.api_key=api
load_dotenv()
completion = openai.Completion()

def replyBrain(question,chat_log=None):
    try:
        FileLog=open("C:\\Users\\priya\\Desktop\\Project-AI(PAI)\\DataBase\\chat_log.txt","r")
        chat_log_template = FileLog.read()
        FileLog.close()

        if chat_log is None:
            chat_log = chat_log_template

        prompt =f'{chat_log}You: {question}\nPAI: '
        response=completion.create(
            model = "text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens = 60,
            top_p=0.3,
            frequency_penalty = 0.5,
            presence_penalty = 0)
        
        answer= response.choices[0].text.strip()
        chat_log_template_update=chat_log_template+f"\nYou: {question}\nPAI: {answer}\n*****************************************************************************\n"
        FileLog=open("C:\\Users\\priya\\Desktop\\Project-AI(PAI)\\DataBase\\chat_log.txt","w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        if answer != None:
            return answer
        else:
            return "I dont want to talk"
    except Exception as e:
        print("Error occured in AI reply:", e)
        pass
    # return translation_to_hindi(answer)

# while True:
#     kk=input("Enter: ")
#     print("PAI: ",replyBrain(kk),"\n")