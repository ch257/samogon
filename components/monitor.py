from components.file_system import FileSystem

class Monitor:
    def __init__(self, errors):
        self.thermometers = [
            {
                'caption' : 't1'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7835/w1_slave"
            }    
            ,{
                'caption' : 't2'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7836/w1_slave"
            }    
            ,{
                'caption' : 't3'
                ,'file_path' : "/sys/devices/w1_bus_master1/28-0120442d7837/w1_slave"
            }    
        ]
        self.errors = errors
        self.file_system = FileSystem(errors)
    
    def get_temperature(self):
        for i in range(len(self.thermometers)):
            file_path = self.thermometers[i]['file_path']
            self.file_system.read_binary_file(file_path)