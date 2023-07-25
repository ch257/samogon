import sys, select
import tty, fcntl, os
import time, termios, atexit

from components.menu import Menu
from components.views import Views
from components.settings import Settings
from components.monitor import Monitor
from components.manager import Manager
from components.errors import Errors

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
settings = Settings(errors)
settings.read_settings('settings/settings.ini')

menu = Menu()
views = Views()
monitor = Monitor(errors, settings)
manager = Manager(errors, settings)
os.system('clear')
views.render_page(menu, settings, monitor, errors)

choice = ''
while True: 
    if kbhit(): # Нажата клавиша
        key = sys.stdin.read(1)
        choice = menu.get_choice(key, manager)
        if choice == 'end':
            break
    
    errors.clear_errors()
    manager.serve(choice)
    monitor.get_temperature()
    monitor.get_state(manager)
    monitor.check_alarms(settings)
    views.render_page(menu, settings, monitor, errors)            
    