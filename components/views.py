class Views:
    def __init__(self):
        self.page_start_line = 1
        self.page_start_col = 1
        self.page_width = 30
        self.menu_height = 5
        self.monitor_height = 7
        
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
        
        for i in range(self.menu_height - len(menu.menu_sections)):
            line_count = line_count + 1
            line = line + self.__make_menu_line(' ', line_count)
        #Print Menu
        print(line)
        
    def __make_monitor_line(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = ' ' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    def __make_monitor_header(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = '-' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    def __render_monitor_frame(self, monitor):
        line = ''
        line_count = self.page_start_line + self.menu_height + 1
        #Monitor Header
        line = line + self.__make_monitor_header('Монитор', line_count)
        #Monitor Body
        for i in range(len(monitor.thermometers)):
            line_count = line_count + 1
            therm = monitor.thermometers[i]
            line = line + self.__make_monitor_line(f"{therm['caption']}: {therm['value']}", line_count)
        
        for i in range(self.monitor_height - len(monitor.thermometers)):
            line_count = line_count + 1
            line = line + self.__make_menu_line(' ', line_count)
        #Print Menu
        print(line)
        
    def __make_errors_line(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1)
    
    def __make_errors_header(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = '-' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    def __render_errors_frame(self, errors):
        line = ''
        line_count = self.page_start_line + self.menu_height + self.monitor_height + 1
        #Monitor Header
        line = line + self.__make_errors_header('Ошибки', line_count)
        #Monitor Body
        for i in range(len(errors.errors_list)):
            line_count = line_count + 1
            line = line + self.__make_errors_line(errors.errors_list[i], line_count)
        
        #Print Menu
        print(line)
        pass
        
        
        
    def render_page(self, menu, monitor, errors):
        self.__render_menu_frame(menu)
        self.__render_monitor_frame(monitor)
        self.__render_errors_frame(errors)
    