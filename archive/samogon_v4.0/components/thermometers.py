from components.file_system import FileSystem

class Thermometers:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__thermometers = []
        self.__thermometer_caption_index = {}

        for i in range(self.__settings['nums']['thermometers_num']):
            thermometer_key = f"thermometer_{i + 1}"
            thermometer_caption = self.__settings[thermometer_key]['caption']
            self.__thermometer_caption_index[thermometer_caption] = i
            self.__thermometers.append({
                'caption' : thermometer_caption
                ,'file_path' : f"/sys/devices/w1_bus_master1/{self.__settings[thermometer_key]['bus_id']}/w1_slave"
                ,'value' : None
            })
        self.__file_system = FileSystem(errors)
        
    def __extract_themperature(self, thermometer):
        themperature = None
        b_line = self.__file_system.read_binary_file(thermometer['file_path'])
        line = b_line.decode('utf-8').replace('\n', '')
        pos = line.find('t=') # Значение температуры после 't='
        if pos != -1:
            themperature = float(line[pos + 2:])/1000
        else:
            if themperature is not None:
                self.errors.add_error(f"Неизвестный формат файла датчика температуры '{thermometer['file_path']}'")
        return themperature
    
    def measure_themperature(self):
        for i in range(len(self.__thermometers)):
            self.__thermometers[i]['value'] = self.__extract_themperature(self.__thermometers[i])
    

    def get_themperature(self, thermometer_caption):
        index = self.__thermometer_caption_index[thermometer_caption]
        return self.__thermometers[index]['value']

    def get_thermometers(self):
        return self.__thermometers