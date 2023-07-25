# python3

import socket
import time

for i in range(10):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 8080))
    client_sock.sendall(b'Hello, world\n')
    # data = client_sock.recv(1024)
    # print('Received', repr(data))
    # client_sock.close()
    time.sleep(5)
