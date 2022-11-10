from components.file_system import FileSystem

class Monitor:
    def __init__(self, errors):
        self.thermometers = [
            {
                'caption' : 't1'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7835/w1_slave"
                ,'value' : ''
            }    
            ,{
                'caption' : 't2'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7836/w1_slave"
                ,'value' : ''
            }    
            ,{
                'caption' : 't3'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7837/w1_slave"
                ,'value' : ''
            }    
        ]
        self.errors = errors
        self.file_system = FileSystem(errors)
    
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