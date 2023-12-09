from openai_agent import OpenAiAgent

class CommandProcessing:

    def __init__(self):
        self.agent = OpenAiAgent()

    def handle_command(self, command):
        return self.agent.get_command_label(command)

