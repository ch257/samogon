from components.file_system import FileSystem
from components.thermometers import Thermometers
from components.relays import Relays

class Monitor:
    def __init__(self, errors, settings):
        self.__settings = settings.get_settings()
        self.__state = 'init'
        self.__errors = errors
        self.__file_system = FileSystem(errors)
        self.__thermometers = Thermometers(errors, settings)
        self.__relays = Relays(errors, settings)
        self.__heating_control_events = []
        for key in self.__settings['heating_control']:
            controller = self.__settings['heating_control'][key]
            controller_relations = controller.split(',')
            thermometer_key = 'thermometer_' + controller_relations[0]
            thermometer = self.__settings[thermometer_key]
            relay_key = 'relay_' + controller_relations[1]
            relay = self.__settings[relay_key]
            self.__heating_control_events.append({
                'controller': key
                ,'thermometer': thermometer_key
                ,'thermometer_caption': thermometer['caption']
                ,'themperature_top_threshold': float(thermometer['heating_control_threshold'])
                ,'themperature_bottom_threshold': float(thermometer['heating_control_threshold']) - float(thermometer['heating_control_hysteresis'])
                ,'relay': relay_key
                ,'relay_bus_id': int(relay['bus_id'])
                ,'relay_top_threshold_signal': relay['open_signal']
                ,'relay_bottom_threshold_signal': relay['closed_signal']
                ,'state': 'heating'
                ,'flag': False
            })
        
        self.__relays.init_relays()
    
    
    def __check_events(self):
        if self.__state == 'heating_control':
            for i in range(len(self.__heating_control_events)):
                event = self.__heating_control_events[i]
                themperature_top_threshold = event['themperature_top_threshold']
                themperature_bottom_threshold = event['themperature_bottom_threshold']
                current_temperature = self.__thermometers.get_themperature(event['thermometer'])
                
                if current_temperature > themperature_top_threshold:
                    event['state'] = 'hot'
                    if not event['flag']:
                        self.__relays.gpio_set_signal(event['relay_bus_id'], event['relay_top_threshold_signal'])
                        event['flag'] = True
                elif current_temperature < themperature_bottom_threshold:
                    event['state'] = 'heating'
                    if event['flag']:
                        self.__relays.gpio_set_signal(event['relay_bus_id'], event['relay_bottom_threshold_signal'])
                        event['flag'] = False
                else: 
                    event['state'] = 'warm'
                    
    
    def watch(self, state):
        self.__state = state
        self.__thermometers.measure_themperature()
        self.__check_events()
    
    def __controller_state_name(self, state):
        if state == 'heating':
            return 'РАЗОГРЕВ'
        elif state == 'warm':
            return 'ГОРЯЧО'
        elif state == 'hot':
            return 'ОПАСНО'
        else:
            return 'НЕИЗВЕСТНО'
    
    def __system_state_name(self):
        if self.__state == 'init':
            return 'Запуск'
        elif self.__state == 'do_nothing':
            return 'Ничего не делаю'
        elif self.__state == 'heating_control':
            return 'Контроль нагрева'
        else:
            return 'НЕИЗВЕСТНО'
    
    def get_view_data(self):
        frame_caption = 'Монитор'
        themperature = self.__thermometers.get_thermometers()
        frame_lines = []
        for i in range(len(themperature)):
            frame_lines.append(f"{themperature[i]['caption']}:{themperature[i]['value']}")
        
        frame_lines.append(f"Состояние:{self.__system_state_name()}")
        
        if self.__state == 'heating_control':    
            for i in range(len(self.__heating_control_events)):
                event = self.__heating_control_events[i]
                frame_lines.append(f"{event['thermometer_caption']}:{self.__controller_state_name(event['state'])}")
        
        
        return {
            'frame_caption': frame_caption
            ,'frame_lines': frame_lines
        }