class Manager:
    def __init__(self, errors, settings, monitor):
        self.__errors = errors
        self.__state = 'do_nothing'
    
    def get_state(self):
        return self.__state
    
    # def set_state(state):
        # self.__state = state

    def serve(self, choice):
        if choice == 'heating_control/set_temperature':
            if self.__state == 'do_nothing':
                pass
        elif choice == 'heating_control/start':
            if self.__state == 'do_nothing':
                self.__state = 'heating_control'
        elif choice == 'heating_control/stop':
            if self.__state == 'heating_control':
                self.__state = 'do_nothing'
        else:
            pass