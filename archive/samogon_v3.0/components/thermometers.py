from components.file_system import FileSystem

THERMOMETERS_NUM = 1

class Thermometers:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__thermometers = []
        for i in range(THERMOMETERS_NUM):
            th_count = str(i + 1)
            self.__thermometers.append({
                'key': 'thermometer_' + th_count
                ,'id': self.__settings['thermometer_' + th_count]['id']
                ,'caption' : self.__settings['thermometer_' + th_count]['caption']
                ,'file_path' : f"/sys/devices/w1_bus_master1/{self.__settings['thermometer_' + th_count]['bus_id']}/w1_slave"
                ,'value' : ''
            })
        self.file_system = FileSystem(errors)
        
    def __extract_themperature(self, file_path):
        themperature = ''
        b_line = self.file_system.read_binary_file(file_path)
        line = b_line.decode('utf-8').replace('\n', '')
        pos = line.find('t=') # Значение температуры после 't='
        if pos != -1:
            themperature = str(float(line[pos + 2:])/1000)
        else:
            if themperature != '':
                self.errors.add_error(f"Неизвестный формат файла датчика температуры '{file_path}'")
        return themperature
    
    def measure_themperature(self):
        for i in range(len(self.__thermometers)):
            file_path = self.__thermometers[i]['file_path']
            self.__thermometers[i]['value'] = self.__extract_themperature(file_path)
    
    def get_thermometers(self):
        return self.__thermometers
    
    def get_themperature(self, thermometer_key):
        for i in range(THERMOMETERS_NUM):
            if self.__thermometers[i]['key'] == thermometer_key:
                return float(self.__thermometers[i]['value'])
