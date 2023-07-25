import RPi.GPIO as GPIO

class Relays:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__relays = []
        self.__relays_caption_index = {}
        for i in range(self.__settings['nums']['relays_num']):
            relay_key = f"relay_{i + 1}"
            self.__relays.append({
                'bus_id' : int(self.__settings[relay_key]['bus_id'])
                ,'caption' : self.__settings[relay_key]['caption']
                ,'init' : self.__settings[relay_key]['init']
                ,'open' : self.__settings[relay_key]['open']
                ,'close' : self.__settings[relay_key]['close']
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
        for i in range(self.__settings['nums']['relays_num']):
            self.__gpio_init(self.__relays[i]['bus_id'], self.__relays[i]['init'])