class Views:
    def __init__(self):
        self.page_start_line = 1
        self.page_start_col = 1
        self.page_width = 30
        self.menu_height = 4
        self.body_height = 7
        
    def __make_menu_line(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = ' ' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    def __make_menu_header(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = '-' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    def __render_menu_frame(self, menu):
        #Menu Vertial Margin
        line = ''
        for i in range(self.page_start_line):
            line = line + self.__make_menu_line(' ' * self.page_width, i)
        #Menu Header
        line_count = self.page_start_line
        line = line + self.__make_menu_header('/'.join(menu.caption_bread_crambs), line_count)
        #Menu Body
        for i in range(len(menu.menu_sections)):
            line_count = line_count + 1
            line = line + self.__make_menu_line(f"[{i}]:{menu.menu_sections[i]['caption']}", line_count)
        #Print Menu
        print(line)
    
    def __render_body_frame(self, lines):
        pass
        
    def render_page(self, menu, body_list=[]):
        self.__render_menu_frame(menu)
        self.__render_body_frame(body_list)
    