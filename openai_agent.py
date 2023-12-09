import openai
from dotenv import load_dotenv
import os 


load_dotenv()
key = os.getenv("API_KEY")

class OpenAiAgent:

    def __init__(self, model="gpt-3.5-turbo", client = openai.OpenAI(api_key=key)):
        self.model = model
        self.client = client

    def get_response(self, command):
        response = self.client.chat.completions.create(
            messages = [
                {"role": "system", "content" : "You are a virtual assistant. Please keep responses minimal"},
                {"role": "user", "content": command}
            ],
            model=self.model
        )


        assistant_reply = response.choices[0].message.content
        return assistant_reply

    def get_command_label(self, command):
        response = self.client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are a virtual assistant. Your role is to classify the user's request as either a to-do item or a general question. For to do item, response 'to do', otherwise response 'normal'"},
                {"role": "user", "content": command}
            ],
            model=self.model
        )

        label = response.choices[0].message.content
        return label