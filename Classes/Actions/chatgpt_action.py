import json
import openai
import os
from dotenv import load_dotenv
from Actions.manual_click_action import ManualClickAction
import time

class ChatGPTAction:
    def __init__(self,midterm=False, prefix= "", filepath="string.txt"):
        
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_KEY')
        self.message = ""
        self.prefix = prefix
        self.filepath = filepath
        self.midterm = midterm
        self.messages = [{"role": "system", "content": "You are a quizz assistant in the game Rise of Kingdoms. You respond only with A, B, C, D or E. Nothing else, ever. Literally only one of those 5 letters. Respond E if you are not sure."}]
        self.functions = [
        {
            "name": "return_option_based_on_prompt",
            "description": "Returns the chosen answer option (A, B, C, D, or E) based on the prompt. Returns 'E' when unsure.",
            "parameters": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "enum": ["A", "B", "C", "D", "E"],
                        "description": "The chosen answer option to the question in the prompt. 'E' is chosen when unsure.",
                    },
                },
                "required": ["answer"],
            },
        }
        ]

    def execute(self):
        
        with open(self.filepath, 'r') as file:
            self.message = file.read()
            print(f"User: {self.message}")
        #concatenate prefix and message
        self.message = self.prefix + self.message
        self.messages.append({"role": "user", "content": (self.message)},)
        chat = openai.ChatCompletion.create(
            model="gpt-4-0613",
            temperature=0.1,
            messages=self.messages,
            functions=self.functions,
            function_call={"name": "return_option_based_on_prompt"}
        )

        response_message = chat.choices[0].message
        print(response_message)

        if response_message.get("function_call"):
            function_arguments = json.loads(response_message["function_call"]["arguments"])
            function_response = function_arguments["answer"]

            # Here function_response should contain the chosen answer
            print(f"ChatGPT: {function_response} \n")
            self.messages.clear()

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
                elif function_response == "E":
                    print("Not Sure")
            else:
                if function_response == "A":
                    ManualClickAction(37,55).execute()
                elif function_response == "B":
                    ManualClickAction(60,55).execute()
                elif function_response == "C":
                    ManualClickAction(37,63).execute()
                elif function_response == "D":
                    ManualClickAction(60,63).execute()
                elif function_response == "E":
                    print("Not Sure")


        time.sleep(2)
        return True
