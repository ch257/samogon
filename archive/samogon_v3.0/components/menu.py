class Menu:
    def __init__(self, errors):
        self.__errors = errors
        self.__menu = [
            {
                'caption' : None
                ,'value' : None
                ,'sections' :[
                    {
                        'caption' : 'Контроль нагрева'
                        ,'value' : 'heating_control'
                        ,'sections' : [
                            {
                                'caption' : 'Настроить температуру'
                                ,'value' : 'set_temperature'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Старт'
                                ,'value' : 'start'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Стоп'
                                ,'value' : 'stop'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Выход'
                                ,'value' : 'exit'
                                ,'sections' : []
                            }
                        ] 
                    }
                    ,{
                        'caption' : 'Первогон'
                        ,'value' : 'pervogon'
                        ,'sections' : [
                            {
                                'caption' : 'Старт'
                                ,'value' : 'start'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Стоп'
                                ,'value' : 'stop'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Выход'
                                ,'value' : 'exit'
                                ,'sections' : []
                            }
                        ] 
                    }
                    ,{
                        'caption' : 'Второгон'
                        ,'value' : 'vtorogon'
                        ,'sections' : [
                            {
                                'caption' : 'Старт'
                                ,'value' : 'start'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Стоп'
                                ,'value' : 'stop'
                                ,'sections' : []
                            }
                            ,{
                                'caption' : 'Выход'
                                ,'value' : 'exit'
                                ,'sections' : []
                            }
                        ]
                    }
                    ,{
                        'caption' : 'Закончить'
                        ,'value' : 'end'
                        ,'sections' : []

                    }
                ]
            }
        ]
        self.__level = 0
        self.__levels = [0]
        self.__menu_sections = self.__menu[self.__levels[self.__level]]['sections']
        self.__caption = self.__menu[self.__levels[self.__level]]['caption']
        self.__value = self.__menu[self.__levels[self.__level]]['value']
        self.__caption_bread_crambs = []
        self.__value_bread_crambs = []
        self.__menu_sections_len = len(self.__menu_sections)
    
    def __menu_down(self, key):
        self.__value = self.__menu_sections[key]['value']
        self.__caption = self.__menu_sections[key]['caption']
        self.__levels.append(key)
        self.__caption_bread_crambs.append(self.__caption)
        self.__value_bread_crambs.append(self.__value)
        self.__level = self.__level + 1
        self.__menu_sections = self.__menu_sections[self.__levels[self.__level]]['sections']
        self.__menu_sections_len = len(self.__menu_sections)
        
    def __menu_up(self):
        self.__level = self.__level - 1
        self.__levels.pop()
        self.__caption_bread_crambs.pop()
        self.__value_bread_crambs.pop()
        for i in range(len(self.__levels)):
            self.__menu_sections = self.__menu[i]['sections']
        self.__caption = self.__menu[self.__levels[self.__level]]['caption']
        self.__value = self.__menu[self.__levels[self.__level]]['value']
        self.__menu_sections_len = len(self.__menu_sections)
    
    def get_choice(self, key, state):
        if key.isdigit():
            key = int(key)
            if key < len(self.__menu_sections):
                value = self.__menu_sections[key]['value']
                value_bread_crambs = '/'.join(self.__value_bread_crambs)
                if value == 'end':
                    return 'end'
                elif value == 'exit':
                    if state == 'do_nothing':
                        self.__menu_up()
                    return value_bread_crambs + '/' + value
                elif value == 'start':
                    return value_bread_crambs + '/' + value
                elif value == 'stop':
                    return value_bread_crambs + '/' + value
                elif value == 'set_temperature':
                    return value_bread_crambs + '/' + value
                else:    
                    self.__menu_down(key)
            
    def get_caption_bread_crambs(self):
        return self.__caption_bread_crambs
    
    def get_value_bread_crambs(self):
        return self.__value_bread_crambs
    
    def get_menu_sections_len(self):
        return self.__menu_sections_len
    
    def get_menu_sections(self):
        return self.__menu_sections
    
    def get_menu_section(self, section_num):
        return self.__menu_sections[section_num]
        
    def get_view_data(self):
        frame_caption = 'Меню'
        if len(self.__caption_bread_crambs) > 0:
            frame_caption = '/'.join(self.__caption_bread_crambs)
        frame_lines = []
        for i in range(len(self.__menu_sections)):
            frame_lines.append(f"[{i}]:{self.__menu_sections[i]['caption']}")
        
        return {
            'frame_caption': frame_caption
            ,'frame_lines': frame_lines
        }
        