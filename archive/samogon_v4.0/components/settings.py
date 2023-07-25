import configparser

class Settings:
    def __init__(self, errors):
        self.__settings = {}
        self.__thermometers_num = 0
        self.__relays_num = 0
        self.__events_num = 0
        self.__actions_num = 0
    
    def __count_entities(self, entity):
        if entity.find('thermometer') != -1:
            self.__thermometers_num = self.__thermometers_num + 1
        elif entity.find('relay') != -1:
            self.__relays_num = self.__relays_num + 1
        elif entity.find('event') != -1:
            self.__events_num = self.__events_num + 1
        elif entity.find('action') != -1:
            self.__actions_num = self.__actions_num + 1
        

    def read_settings(self, settings_filepath):
        self.__settings = {}
        config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation(),
            allow_no_value=True,
            delimiters='=',
            inline_comment_prefixes='#'
        )
        config.optionxform = str
        config.read(settings_filepath)
        for section in config.sections():
            self.__settings[section] = {}
            self.__count_entities(section)
            for option in config.options(section):
                self.__settings[section][option] = config[section][option]
        
        self.__settings['nums'] = {
            'thermometers_num': self.__thermometers_num
            ,'relays_num': self.__relays_num
            ,'events_num': self.__events_num
            ,'actions_num': self.__actions_num
        }
                
    def get_settings(self):
        return self.__settings
    
    # def __read_controller_relations(self, controller, menu_value):
        # line = ''
        # if menu_value == 'heating_control':
            # controller_relations = controller.split(',')
            # thermometer_key = 'thermometer_' + controller_relations[0]
            # th_caption = self.__settings[thermometer_key]['caption']
            # th_heating_control_threshold = float(self.__settings[thermometer_key]['heating_control_threshold'])
            # th_heating_control_hysteresis = float(self.__settings[thermometer_key]['heating_control_hysteresis'])
            # th_top_threshold = th_heating_control_threshold
            # th_bottom_threshold = th_heating_control_threshold - th_heating_control_hysteresis
            
            # relay_key = 'relay_' + controller_relations[1]
            # r_caption = self.__settings[relay_key]['caption']
            # r_open_signal = self.__settings[relay_key]['open_signal']
            # r_closed_signal = self.__settings[relay_key]['closed_signal']
            
            # line = line + f"{th_caption} > {th_top_threshold} => {r_caption}:{r_open_signal}, "
            # line = line + f"{th_caption} < {th_bottom_threshold} => {r_caption}:{r_closed_signal}"
            
        # return line
    
    def get_view_data(self, menu_values):
        frame_caption = 'Настройки'
        frame_lines = []
        if len(menu_values) > 0:
            if menu_values[0] == 'heating_control':
                settings = self.__settings[menu_values[0]]
                for key in (settings):
                    frame_lines.append(self.__read_controller_relations(settings[key], menu_values[0]))
            
        return {
            'frame_caption': frame_caption
            ,'frame_lines': frame_lines
        }
        
        
        