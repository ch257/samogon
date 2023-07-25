class Actions:
    
    def __init__(self, errors, settings):
        self.__errors = errors
        self.__settings = settings.get_settings()
        self.__actions = []
        self.__actions_caption_index = {}
        for i in range(self.__settings['nums']['actions_num']):
            action_key = f"action_{i + 1}"
            self.__actions.append({
                'caption' : self.__settings[action_key]['caption']
                ,'action' : self.__settings[action_key]['action']
            })
