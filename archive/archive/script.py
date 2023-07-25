import sys, select
import tty, fcntl, os
import time, termios, atexit

timeout = 300
menu = [
    {
        'caption' : None
        ,'value' : None
        ,'sections' :[
            {
                'caption' : 'Первогон'
                ,'value' : 'pervogon'
                ,'sections' : [
                    {
                        'caption' : 'Старт'
                        ,'value' : 'start'
                        ,'sections' : []
                    }
                    ,{
                        'caption' : 'Стоп'
                        ,'value' : 'stop'
                        ,'sections' : []
                    }
                    ,{
                        'caption' : 'Выход'
                        ,'value' : 'exit'
                        ,'sections' : []
                    }
                ] 
            }
            ,{
                'caption' : 'Второгон'
                ,'value' : 'vtorogon'
                ,'sections' : [
                    {
                        'caption' : 'Старт'
                        ,'value' : 'start'
                        ,'sections' : []
                    }
                    ,{
                        'caption' : 'Стоп'
                        ,'value' : 'stop'
                        ,'sections' : []
                    }
                    ,{
                        'caption' : 'Выход'
                        ,'value' : 'exit'
                        ,'sections' : []
                    }
                ]
            }
            ,{
                'caption' : 'Кончить'
                ,'value' : 'exit'
                ,'sections' : []

            }
        ]
    }
]

def print_menu(menu_sections):
    for i in range(len(menu_sections)):
        print(f"\033[%d;%dH[{i}]:{menu_sections[i]['caption']}                     " % (i+1,1))
    
def print_page(page_start_line, page_stop_line):
    for i in range(page_start_line, page_stop_line):
        print(f"\033[%d;%dH\n                     " % (i+1,1))
    
def menu_up(d, caption, choice, level):
    levels.append(d)
    caption_bread_crambs.append(caption)
    choice_bread_crambs.append(choice)
    level = level + 1
    return level, menu_sections[levels[level]]['sections']
        
def menu_down(level):
    level = level - 1
    levels.pop()
    menu_sections = None
    for i in range(len(levels)):
        menu_sections = menu[i]['sections']
    return level, menu_sections

def kbhit(): # Проверка нажата ли клавиша
    return poller.poll(timeout)

def restore_term(): # Возврат к старому терминалу (для регистрации в atexit())
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)



        
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
atexit.register(restore_term)
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
tty.setcbreak(sys.stdin)
fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)


level = 0
levels = [0]
menu_sections = menu[levels[level]]['sections']

os.system('clear')
print_menu(menu_sections)

caption_bread_crambs = []
choice_bread_crambs = []

new_mode = 'do_nothing'

count = 0
while True: 
    # Обрабатываем состояние клавиатуры
    if kbhit(): # Нажата клавиша
        d = sys.stdin.read(1)
        if d.isdigit():
            d = int(d) 
            choice = menu_sections[d]['value']
            caption = menu_sections[d]['caption']
            # print('choice = ', choice)
            # print('caption = ', caption)
            if choice == 'exit':
                if level == 0:
                    break
                else:
                    level, menu_sections = menu_down(level)
            elif choice == 'start':
                if '/'.join(choice_bread_crambs) == 'pervogon':
                    new_mode = 'pervogon_started'
                elif '/'.join(choice_bread_crambs) == 'vtorogon':
                    new_mode = 'vtorogon_started'
            elif choice == 'stop':
                if '/'.join(choice_bread_crambs) == 'pervogon':
                    new_mode = 'pervogon_stopped'
                elif '/'.join(choice_bread_crambs) == 'vtorogon':
                    new_mode = 'vtorogon_stopped'
            else:    
                level, menu_sections = menu_up(d, caption, choice, level)
            
            print_menu(menu_sections)
        
        
               
    if new_mode == "pervogon_started":
        print_page(5, 10)   
    elif new_mode == "vtorogon_started":
        pass
    elif new_mode == "pervogon_stopped":
        pass
    elif new_mode == "vtorogon_stopped":
        pass
    elif new_mode == "vtorogon_started":
        pass
    
    count = count + 1
    print(count)