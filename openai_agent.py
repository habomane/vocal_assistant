import openai
from dotenv import load_dotenv
import os 


load_dotenv()
openai.api_key = os.getenv("API_KEY")

class OpenAiAgent:

    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def get_response(self, command):
        response = openai.ChatCompletion.create(
            model=self.model,
            message = [
                {"role": "system", "content": "You are a vocal assistant. Answer is a sufficient and concise way and should not take more than 30 seconds to respond."},
                {"role": "user", "content": command}
            ]
        )

        assistant_reply = response["choices"][0]["message"]["content"]
        return assistant_reply

    