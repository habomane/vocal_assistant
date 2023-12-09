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
            if command == "get current to-do list":
                todo_list = self.todo_manager.get_todo_list_str()
                self.speech_processor.speak(todo_list)

            elif command != "":
                ##get inquiry type
                label = self.command_processor.handle_command(command)
                if label != "normal":
                    self.todo_manager.add_to_todo_list(command)

                ##get API response 
                response = self.openai_agent.get_response(command)
                self.speech_processor.speak(response)
            


if __name__ == "__main__":
    app = MainApp()
    app.run()
