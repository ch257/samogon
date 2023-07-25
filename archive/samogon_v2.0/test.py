import sys, select
import tty, fcntl, os
import time, termios, atexit
import smbus

import RPi.GPIO as GPIO

timeout = 300
mode = "nothing"
temp_filepath_1 = "/sys/devices/w1_bus_master1/28-012043e9b0ed/w1_slave"

high_temp = 30
low_temp = 29
GPIO_num = 26

def kbhit(): # Проверка нажата ли клавиша
    return poller.poll(timeout)

def restore_term(): # Возврат к старому терминалу (для регистрации в atexit())
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)
    
def read_binary_file(filepath):
    file = open(filepath, mode='rb')
    b_line = file.read()
    file.close()
    return b_line

def parse_temperature(b_line):
    line = b_line.decode('utf-8').replace('\n', '')
    pos = line.find('t=') # Значение температуры после 't='
    if pos != -1:
        return float(line[pos + 2:])/1000
    
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
atexit.register(restore_term)
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
tty.setcbreak(sys.stdin)
fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)


print("press 'q' to quit")
print("press 'm' to start monitoring")
print("press 's' to stop monitoring")
print("press 't' to test")


print('INIT BY LOW')
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_num, GPIO.OUT, initial=GPIO.LOW)
   
while True: # Поехали...

    # Обрабатываем состояние клавиатуры
    if kbhit(): # Нажата клавиша
        ch = sys.stdin.read(1)
        if ch == 'q': # Если q, то выходим из цикла. Это конец работы
            print("bye!")
            break
        elif ch == 'm':
            print("start monitoring")
            mode = "monitor"
        elif ch == 's':
            print("stop monitoring")
            mode = "nothing"
        elif ch == 't':
            print("run test")
            mode = "test"
    
    if mode == "monitor":
        temp_1 = parse_temperature(read_binary_file(temp_filepath_1))
        # print(temp_1)
        if temp_1 != None:
            if temp_1 > high_temp:
                print(temp_1, "HOT")
                GPIO.output(GPIO_num, GPIO.HIGH)
            elif temp_1 < low_temp:
                print(temp_1, "NORMAL")
                GPIO.output(GPIO_num, GPIO.LOW)
            else:
                print(temp_1, "WARM")
    elif mode == "test":
        sleep_time = 1
        for i in range(2):
            time.sleep(sleep_time)
            print('HIGH')
            GPIO.setup(GPIO_num, GPIO.OUT, initial=GPIO.HIGH)

            time.sleep(1)
            print('LOW')
            GPIO.setup(GPIO_num, GPIO.OUT, initial=GPIO.LOW)

        print("stop test")
        mode = "nothing"
        
GPIO.cleanup()