import RPi.GPIO as GPIO

RELAYS_NUM = 1

class Relays:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__relays = []
        for i in range(RELAYS_NUM):
            r_count = str(i + 1)
            self.__relays.append({
                'key': 'relay_' + r_count
                ,'id': self.__settings['relay_' + r_count]['id']
                ,'bus_id' : int(self.__settings['relay_' + r_count]['bus_id'])
                ,'caption' : self.__settings['relay_' + r_count]['caption']
                ,'init_signal' : self.__settings['relay_' + r_count]['init_signal']
                ,'open_signal' : self.__settings['relay_' + r_count]['open_signal']
                ,'closed_signal' : self.__settings['relay_' + r_count]['closed_signal']
            })
        GPIO.setmode(GPIO.BCM)
        
    def gpio_set_signal(self, bus_id, signal):
        if signal == 'LOW':
            GPIO.output(bus_id, GPIO.LOW)
        elif signal == 'HIGH':
            GPIO.output(bus_id, GPIO.HIGH)
    
    def __gpio_init(self, bus_id, signal):
        if signal == 'LOW':
            GPIO.setup(bus_id, GPIO.OUT, initial=GPIO.LOW)
        elif signal == 'HIGH':
            GPIO.setup(bus_id, GPIO.OUT, initial=GPIO.HIGH)
            
    
    def init_relays(self):
        for i in range(RELAYS_NUM):
            self.__gpio_init(self.__relays[i]['bus_id'], self.__relays[i]['init_signal'])