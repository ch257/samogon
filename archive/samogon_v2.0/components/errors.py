class Errors:
    def __init__(self):
        self.errors_list = []
    
    def clear_errors(self):
        self.errors_list = []
    
    def add_error(self, description):
        self.errors_list.append(description)