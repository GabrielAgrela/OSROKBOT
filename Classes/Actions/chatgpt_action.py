import json
from Actions.action import Action
import openai
import os
from dotenv import load_dotenv
from Actions.manual_click_action import ManualClickAction
import time
from termcolor import colored
import os
from global_vars import GlobalVars


class ChatGPTAction(Action):
    def __init__(self,midterm=False, filepath="string.txt", delay=0, retard =0):
        
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_KEY')
        self.message = ""
        self.midterm = midterm
        self.delay = delay
        self.retard = retard
        self.messages = [{"role": "system", "content": "You are a quizz assistant in the game Rise of Kingdoms."}]
        self.functions = [
        {
            "name": "return_option_based_on_prompt",
            "description": "thinking step by step, ignoring the answer options, returns the chosen answer option (A, B, C or D) based on the prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "enum": ["A", "B", "C", "D"],
                        "description": "The chosen answer option to the question in the prompt.",
                    },
                },
                "required": ["answer"],
            },
        }
        ]
                    
    def execute(self):
        #os.system('cls')
        self.message = "Question:" +  GlobalVars().Q + "\n" + "A:" + GlobalVars().A + "\n" + "B:" + GlobalVars().B + "\n" + "C:" + GlobalVars().C + "\n" + "D:" + GlobalVars().D
        print("\n\n")
        self.messages.append({"role": "user", "content": (self.message)},)
        chat = openai.ChatCompletion.create(
            model="gpt-4-0613",
            temperature=1,
            messages=self.messages,
            functions=self.functions,
            function_call={"name": "return_option_based_on_prompt"}
        )

        response_message = chat.choices[0].message
        

        if response_message.get("function_call"):
            function_arguments = json.loads(response_message["function_call"]["arguments"])
            function_response = function_arguments["answer"]

            print("\n\n I think it's " , colored(function_response,"red"))

            self.messages.clear()
            self.messages = [{"role": "system", "content": "You are a quizz assistant in the game Rise of Kingdoms."}]

            # Switch case for reply A, B, C, D, or E
            if not self.midterm:
                if function_response == "A":
                    ManualClickAction(40,48).execute()
                elif function_response == "B":
                    ManualClickAction(60,50).execute()
                elif function_response == "C":
                    ManualClickAction(40,58).execute()
                elif function_response == "D":
                    ManualClickAction(60,58).execute()
                else:
                    print("")
                
            else:
                if function_response == "A":
                    ManualClickAction(37,55).execute()
                elif function_response == "B":
                    ManualClickAction(60,55).execute()
                elif function_response == "C":
                    ManualClickAction(37,63).execute()
                elif function_response == "D":
                    ManualClickAction(60,63).execute()
                

        
        return True
