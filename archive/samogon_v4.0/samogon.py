import sys, select
import tty, fcntl, os
import time, termios, atexit
import RPi.GPIO as GPIO

from components.errors import Errors
from components.menu import Menu
from components.manager import Manager
from components.settings import Settings
from components.views import Views
from components.monitor import Monitor

TIMEOUT = 100


def kbhit(): # Проверка нажата ли клавиша
    return poller.poll(TIMEOUT)

def restore_term(): # Возврат к старому терминалу (для регистрации в atexit())
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)
        
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
atexit.register(restore_term)
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
tty.setcbreak(sys.stdin)
fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

errors = Errors()
menu = Menu(errors)
settings = Settings(errors)
settings.read_settings('settings/settings.ini')
monitor = Monitor(errors, settings)
manager = Manager(errors, settings, monitor)
views = Views(errors)

os.system('clear')
views.render_page(menu, settings, monitor, errors)

choice = ''

count = 0
while True: 
    state = manager.get_state()
    if kbhit(): # Нажата клавиша
        key = sys.stdin.read(1)
        choice = menu.get_choice(key, state)
        if choice == 'end':
            GPIO.cleanup()
            break
    
    errors.clear_errors()
    manager.serve(choice)
    monitor.watch(state)
    views.render_page(menu, settings, monitor, errors)
    
    #Debug
    if count > 1:
        break
    count = count + 1
    

    