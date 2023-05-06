#Api key
fileopen = open("Data\\api.txt","r")
api=fileopen.read()
fileopen.close()

#importing
import openai
from dotenv import load_dotenv

#coding

openai.api_key=api
load_dotenv()
completion = openai.Completion()

def questionAnswer(question,chat_log=None):
    try:
        FileLog=open("C:\\Users\\priya\\Desktop\\Project-AI(PAI)\\DataBase\\qna_log.txt","r")
        chat_log_template = FileLog.read()
        FileLog.close()

        if chat_log is None:
            chat_log = chat_log_template

        prompt =f'{chat_log}Question: {question}\nAnswer: '
        response=completion.create(
            model = "text-davinci-002",
            prompt=prompt,
            temperature=0,
            max_tokens = 100,
            top_p=1,
            frequency_penalty = 0,
            presence_penalty = 0)
        
        answer= response.choices[0].text.strip()
        chat_log_template_update=chat_log_template+f"\nQuestion: {question}\nAnswer: {answer}"
        FileLog=open("C:\\Users\\priya\\Desktop\\Project-AI(PAI)\\DataBase\\qna_log.txt","w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        if answer != None:
            return answer
        else:
            return ""
    except Exception as e:
        print("An error occured in AI QnA: ",e)
        pass
