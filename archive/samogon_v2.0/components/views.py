class Views:
    def __init__(self):
        self.page_start_line = 1
        self.page_start_col = 1
        self.page_width = 100
        self.menu_frame_height = 6
        self.settings_frame_height = 7
        self.monitor_frame_height = 8
        self.errors_frame_height = 20
        
        self.states = {
            'init': 'Init'
            ,'do_nothing': 'Ничего не делаю'
            ,'heating_control': 'Запущен контроль нагрева'
        }
        
    def __make_frame_header(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = '-' * (self.page_width - self.page_start_col - len(line))
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix

    def __make_frame_line(self, line, line_count):
        line_prefix = ' ' * (self.page_start_col - 1)
        line_suffix = ''
        suffix_fillings_number = self.page_width - self.page_start_col - len(line)
        if suffix_fillings_number > 0:
            line_suffix = ' ' * suffix_fillings_number
        return f"\033[%d;%dH{line_prefix}{line}" % (line_count, 1) + line_suffix
    
    #=========== Menu Frame    
    def __render_menu_frame(self, menu):
        #Menu Vertial Margin
        line = ''
        for i in range(self.page_start_line):
            line = line + self.__make_frame_line(' ' * self.page_width, i)
        #Menu Header
        line_count = self.lines_count
        line = line + self.__make_frame_header('/'.join(menu.caption_bread_crambs), line_count)
        #Menu Body
        for i in range(len(menu.menu_sections)):
            line_count = line_count + 1
            line = line + self.__make_frame_line(f"[{i}]:{menu.menu_sections[i]['caption']}", line_count)
        
        for i in range(self.menu_frame_height - len(menu.menu_sections)):
            line_count = line_count + 1
            line = line + self.__make_frame_line('', line_count)
        
        self.lines_count = self.lines_count + self.menu_frame_height + 1
        #Print Menu
        print(line)

    #=========== Settings Frame    
    def __make_settings_list(self, settings, menu):
        settings_list = []
        menu_value = '/'.join(menu.value_bread_crambs)
        if menu_value == 'heating_control':
            selected_menu_settings = settings.settings[menu_value]
            for key in selected_menu_settings:
                settings_list.append(f"{settings.settings[key]['caption']} = {selected_menu_settings[key]}")
        return settings_list
    
    def __render_settings_frame(self, settings, menu):
        line = ''
        line_count = self.lines_count
        #Settings Header
        line = line + self.__make_frame_header('Настройки', line_count)
        #Settings Body
        settings_list = self.__make_settings_list(settings, menu)
        for i in range(len(settings_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line(settings_list[i], line_count)
            
        for i in range(self.settings_frame_height - len(settings_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line('', line_count)
        
        self.lines_count = self.lines_count + self.settings_frame_height + 1
        #Print Settings
        print(line)
    
    #=========== Monitor Frame
    def __make_monitor_list(self, monitor):
        monitor_list = []
        for i in range(len(monitor.thermometers)):
            therm = monitor.thermometers[i]
            monitor_list.append(f"{therm['caption']}: {therm['value']}")
        
        monitor_list.append(f"Состояние: {self.states[monitor.state]}")
        
        for i in range(len(monitor.alarms)):
            monitor_list.append(f"{monitor.alarms[i]}")
        
        return monitor_list
    
    def __render_monitor_frame(self, monitor):
        line = ''
        line_count = self.lines_count
        #Monitor Header
        line = line + self.__make_frame_header('Монитор', line_count)
        #Monitor Body
        monitor_list = self.__make_monitor_list(monitor)
        for i in range(len(monitor_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line(monitor_list[i], line_count)
        
        for i in range(self.monitor_frame_height - len(monitor_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line('', line_count)
            
        self.lines_count = self.lines_count + self.monitor_frame_height + 1
        #Print Monitor
        print(line)
        
    #=========== Error Frame    
    def __render_errors_frame(self, errors):
        line = ''
        line_count = self.lines_count
        #Errors Header
        line = line + self.__make_frame_header('Ошибки', line_count)
        #Errors Body
        for i in range(len(errors.errors_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line(errors.errors_list[i], line_count)
        
        for i in range(self.errors_frame_height - len(errors.errors_list)):
            line_count = line_count + 1
            line = line + self.__make_frame_line('', line_count)
        #Print Errors
        print(line)
        
    
        
    def render_page(self, menu, settings, monitor, errors):
        # errors.add_error(f"Debugging: {'/'.join(menu.value_bread_crambs)}")
        self.lines_count = self.page_start_line
        self.__render_menu_frame(menu)
        self.__render_settings_frame(settings, menu)
        self.__render_monitor_frame(monitor)
        self.__render_errors_frame(errors)
    