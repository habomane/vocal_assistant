import command_processing as cp
import openai_agent as oagent
import speech_processing as sp
import todo_manager as tdmanager


class MainApp:

    def __init__(self):
        self.speech_processor = sp.SpeechProcessing()
        self.command_processor = cp.CommandProcessing()
        self.openai_agent = oagent.OpenAiAgent()
        self.todo_manager = tdmanager.ToDoManager()

    def run(self):
        while True:
            command = self.speech_processor.listen()
            if command != "":
                response = self.openai_agent.get_response(command)
                print("ChatGPT answered:", response)
            


if __name__ == "__main__":
    app = MainApp()
    app.run()
