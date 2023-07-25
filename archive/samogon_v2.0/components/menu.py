class Menu:
    def __init__(self):
        self. menu = [
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
        self.level = 0
        self.levels = [0]
        self.menu_sections = self.menu[self.levels[self.level]]['sections']
        self.caption = self.menu[self.levels[self.level]]['caption']
        self.value = self.menu[self.levels[self.level]]['value']
        self.caption_bread_crambs = []
        self.value_bread_crambs = []
        
    def __menu_down(self, key):
        self.value = self.menu_sections[key]['value']
        self.caption = self.menu_sections[key]['caption']
        self.levels.append(key)
        self.caption_bread_crambs.append(self.caption)
        self.value_bread_crambs.append(self.value)
        self.level = self.level + 1
        self.menu_sections = self.menu_sections[self.levels[self.level]]['sections']
        
    def __menu_up(self):
        self.level = self.level - 1
        self.levels.pop()
        self.caption_bread_crambs.pop()
        self.value_bread_crambs.pop()
        for i in range(len(self.levels)):
            self.menu_sections = self.menu[i]['sections']
        self.caption = self.menu[self.levels[self.level]]['caption']
        self.value = self.menu[self.levels[self.level]]['value']
    
    def get_choice(self, key, manager):
        if key.isdigit():
            key = int(key)
            if key < len(self.menu_sections):
                value = self.menu_sections[key]['value']
                value_bread_crambs = '/'.join(self.value_bread_crambs)
                if value == 'end':
                    return 'end'
                elif value == 'exit':
                    if manager.state == 'do_nothing':
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
            
    
    