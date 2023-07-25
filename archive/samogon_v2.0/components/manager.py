class Manager:
    def __init__(self, errors, settings):
        self.errors = errors
        self.state = 'do_nothing'

    def serve(self, choice):
        
        if choice == 'heating_control/set_temperature':
            if self.state == 'do_nothing':
                pass
        elif choice == 'heating_control/start':
            if self.state == 'do_nothing':
                self.state = 'heating_control'
        elif choice == 'heating_control/stop':
            if self.state == 'heating_control':
                self.state = 'do_nothing'
        else:
            pass