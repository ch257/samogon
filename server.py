import asyncio
# import sys, select
# import tty, fcntl, os
# import time, termios, atexit
# import RPi.GPIO as GPIO


from components.errors import Errors
# from components.menu import Menu
# from components.manager import Manager
from components.settings import Settings
# from components.views import Views
# from components.monitor import Monitor

from components.thermometers import Thermometers


errors = Errors()
# menu = Menu(errors)
settings = Settings(errors)
settings.read_settings('settings/settings.ini')
# monitor = Monitor(errors, settings)
# manager = Manager(errors, settings, monitor)
# views = Views(errors)

thermometers = Thermometers(errors, settings)
async def main():
    await thermometers.measure_themperature()

    # print(thermometers.get_thermometers())
    print(thermometers.get_themperature("Куб"))
    print(errors.get_errors())
    
asyncio.run(main())



    

    