from components.file_system import FileSystem

class Monitor:
    def __init__(self, errors, settings):
        self.thermometers = [
            {
                'key': 'termometer_1'
                ,'caption' : settings.settings['termometer_1']['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{settings.settings['termometer_1']['id']}/w1_slave"
                ,'value' : ''
            }    
            ,{
                'key': 'termometer_2'
                ,'caption' : settings.settings['termometer_2']['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{settings.settings['termometer_2']['id']}/w1_slave"
                ,'value' : ''
            }    
            ,{
                'key': 'termometer_3'
                ,'caption' : settings.settings['termometer_3']['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{settings.settings['termometer_3']['id']}/w1_slave"
                ,'value' : ''
            }    
            ,{
                'key': 'termometer_4'
                ,'caption' : settings.settings['termometer_4']['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{settings.settings['termometer_4']['id']}/w1_slave"
                ,'value' : ''
            }    
            ,{
                'key': 'termometer_5'
                ,'caption' : settings.settings['termometer_5']['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{settings.settings['termometer_5']['id']}/w1_slave"
                ,'value' : ''
            }    
        ]
        self.state = 'init'
        self.errors = errors
        self.file_system = FileSystem(errors)
        self.alarms = []
        self.temperature_alarms = [
            {
                'key': 'termometer_1'
                ,'description' : ''
                ,'alarm' : 'no'
            }    
            ,{
                'key': 'termometer_2'
                ,'description' : ''
                ,'alarm' : 'no'
            }    
            ,{
                'key': 'termometer_3'
                ,'description' : ''
                ,'alarm' : 'no'
            }    
            ,{
                'key': 'termometer_4'
                ,'description' : ''
                ,'alarm' : 'no'
            }    
            ,{
                'key': 'termometer_5'
                ,'description' : ''
                ,'alarm' : 'no'
            }    

        ]
    
    def __extract_temperature(self, file_path):
        temperature = ''
        b_line = self.file_system.read_binary_file(file_path)
        line = b_line.decode('utf-8').replace('\n', '')
        pos = line.find('t=') # Значение температуры после 't='
        if pos != -1:
            temperature = str(float(line[pos + 2:])/1000)
        else:
            if temperature != '':
                self.errors.add_error(f"Неизвестный формат файла датчика температуры '{file_path}'")
        return temperature
    
    def get_temperature(self):
        for i in range(len(self.thermometers)):
            file_path = self.thermometers[i]['file_path']
            self.thermometers[i]['value'] = self.__extract_temperature(file_path)
            
    def get_state(self, manager):
        self.state = manager.state
        
    def __index_by_key(self, key, items_list):
        for i in range(len(items_list)):
            if items_list[i]['key'] == key:
                return i
                
    def __get_termometer_value(self, key):
        return self.thermometers[self.__index_by_key(key, self.thermometers)]['value']
        
    def __get_temperature_alarm_item_by_field(self, key, field):
        return self.temperature_alarms[self.__index_by_key(key, self.temperature_alarms)][field]
    
    def __set_temperature_alarm_item_by_field(self, key, field, value):
        self.temperature_alarms[self.__index_by_key(key, self.temperature_alarms)][field] = value
    
    def check_alarms(self, settings):
        self.alarms = []
        if self.state == 'heating_control':
            selected_menu_settings = settings.settings[self.state]
            for key in selected_menu_settings:
                termometer_value = float(self.__get_termometer_value(key)) 
                termometer_settings = selected_menu_settings[key].split("-")
                temperature_alarm = self.__get_temperature_alarm_item_by_field(key, 'alarm')
                if temperature_alarm == 'yes':
                    if float(termometer_settings[0]) - float(termometer_settings[1]) > termometer_value:
                        self.__set_temperature_alarm_item_by_field(key, 'alarm', 'no')
                    else:
                        self.alarms.append(f"Критическая температура: {settings.settings[key]['caption']} = {termometer_value}")
                else:
                    if float(termometer_settings[0]) < termometer_value:
                        self.__set_temperature_alarm_item_by_field(key, 'alarm', 'yes')
                        self.alarms.append(f"Критическая температура: {settings.settings[key]['caption']} = {termometer_value}")
        
        