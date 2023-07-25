PAGE_START_LINE = 0
PAGE_START_COL = 0
PAGE_WIDTH = 100
MENU_FRAME_HEIGHT = 6
SETTINGS_FRAME_HEIGHT = 7
MONITOR_FRAME_HEIGHT = 12
ERRORS_FRAME_HEIGHT = 20

class Views:
    
    def __init__(self, errors):
        self.__errors = errors
        self.__states = {
            'init': 'Init'
            ,'do_nothing': 'Ничего не делаю'
            ,'heating_control': 'Запущен контроль нагрева'
        }
        self.__lines_count = 0
        
    def __make_frame_caption(self, line, line_count):
        line_prefix = ' ' * (PAGE_START_COL - 1)
        line_suffix = '-' * (PAGE_WIDTH - PAGE_START_COL - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix

    def __make_frame_line(self, line, line_count):
        line_prefix = ' ' * (PAGE_START_COL - 1)
        line_suffix = ''
        suffix_fillings_number = PAGE_WIDTH - PAGE_START_COL - len(line)
        if suffix_fillings_number > 0:
            line_suffix = ' ' * suffix_fillings_number
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    #Vertical Margin    
    def __render_vertical_margin(self, frame_height):
        #Vertical Margin
        line = ''
        for i in range(frame_height):
            line = line + self.__make_frame_line(' ' * PAGE_WIDTH, i)
        self.__lines_count = self.__lines_count + frame_height + 1
        
    #Frame    
    def __render_frame(self, view_data, frame_height):
        line = ''
        
        #Caption
        line_count = self.__lines_count
        line = line + self.__make_frame_caption(view_data['frame_caption'], line_count)
        
        #Body Data
        lines_number = len(view_data['frame_lines'])
        for i in range(lines_number):
            line_count = line_count + 1
            line = line + self.__make_frame_line(view_data['frame_lines'][i], line_count)
        
        #Body Remains
        for i in range(frame_height - lines_number):
            line_count = line_count + 1
            line = line + self.__make_frame_line('', line_count)
        
        self.__lines_count = self.__lines_count + frame_height + 1
        
        #Print Frame
        print(line)

    def render_page(self, menu, settings, monitor, errors):
        # errors.add_error(f"Debugging: {'/'.join(menu.value_bread_crambs)}")
        #Vertical Margin 
        self.__lines_count = 0
        self.__render_vertical_margin(PAGE_START_LINE)
        #Menu
        view_data = menu.get_view_data()
        self.__render_frame(view_data, MENU_FRAME_HEIGHT)
        #Settings
        view_data = settings.get_view_data(menu.get_value_bread_crambs())
        self.__render_frame(view_data, SETTINGS_FRAME_HEIGHT)
        #Monitor
        view_data = monitor.get_view_data()
        self.__render_frame(view_data, MONITOR_FRAME_HEIGHT)
        #Errors
        view_data = errors.get_view_data()
        self.__render_frame(view_data, ERRORS_FRAME_HEIGHT)
    