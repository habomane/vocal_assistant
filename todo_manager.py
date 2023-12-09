class ToDoManager:

    def __init__(self, list=[]):
        self.current_todo_list = list

    def add_to_todo_list(self, item):
        self.current_todo_list.append(item)
    
    def get_todo_list(self):
        return self.current_todo_list
    
    def get_todo_list_str(self):
        todo_list_str = "Your current to do list includes"
        for item in self.current_todo_list:
            todo_list_str+= item
        
        return todo_list_str
        
    

