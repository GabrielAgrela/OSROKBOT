import openai
import os
from dotenv import load_dotenv
from Actions.manual_click_action import ManualClickAction
import time

class ChatGPTAction:
    def __init__(self, prefix= "", filepath="string.txt"):
        
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_KEY')
        self.message = ""
        self.prefix = prefix
        self.filepath = filepath
        self.messages = [{"role": "system", "content": "You are a quizz assistant in the game Rise of Kingdoms. You respond only with A, B, C, D or E. Nothing else, ever. Literally only one of those 5 letters. Respond E if you are not sure."}]

    def execute(self):
        with open(self.filepath, 'r') as file:
            self.message = file.read()
            print(f"User: {self.message}")
        #concatenate prefix and message
        self.message = self.prefix + self.message
        self.messages.append({"role": "user", "content": (self.message)},)
        chat = openai.ChatCompletion.create(model="gpt-4",max_tokens=1, messages=self.messages)
        reply = chat.choices[0].message.content
        
        print(f"ChatGPT: {reply} \n")
        self.messages.clear()
        time.sleep(2)
        # switch case for reply a b c d
        if reply == "A":
            ManualClickAction(40,48).execute()
        if reply == "B":
            ManualClickAction(60,50).execute()
        if reply == "C":
            ManualClickAction(40,58).execute()
        if reply == "D":
            ManualClickAction(60,58).execute()
        if reply == "E":
            print("Not Sure")
        time.sleep(2)
        return True
