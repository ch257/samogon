import configparser

class Settings:
    def __init__(self, errors):
        self.settings = {}

    def read_settings(self, settings_filepath):
        self.settings = {} 
        config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation(),
            allow_no_value=True,
            delimiters='=',
            inline_comment_prefixes='#'
        )
        config.optionxform = str
        config.read(settings_filepath)
        for section in config.sections():
            self.settings[section] = {}
            for option in config.options(section):
                self.settings[section][option] = config[section][option]
    
    