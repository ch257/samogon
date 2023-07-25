class Events:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__events = []
        self.__events_caption_index = {}
        for i in range(self.__settings['nums']['events_num']):
            event_key = f"event_{i + 1}"
            self.__events.append({
                'caption' : self.__settings[event_key]['caption']
                ,'thermometer' : self.__settings[event_key]['thermometer']
                ,'themperature' : self.__settings[event_key]['themperature']
            })
