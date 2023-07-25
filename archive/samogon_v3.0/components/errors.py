class Errors:
    def __init__(self):
        self.__errors = []
    
    def clear_errors(self):
        self.__errors = []
    
    def add_error(self, description):
        self.__errors.append(description)
    
    def get_errors(self):
        return self.__errors
    
    def get_error_item(self, item_num):
        return self.__errors[item_num]
        
    def get_errors_list_len(self):
        return len(self.__errors)
    
    def get_view_data(self):
        frame_caption = 'Ошибки'
        frame_lines = []
        for i in range(len(self.__errors)):
            frame_lines.append(f"{self.__errors[i]}")
        
        return {
            'frame_caption': frame_caption
            ,'frame_lines': frame_lines
        }