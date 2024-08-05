import socket
import sys
import os
from time import sleep

SERVER_IP = '127.0.0.1'
SERVER_PORT = 2222
address = (SERVER_IP,SERVER_PORT)

fileName = sys.argv[1]
fileSize = os.path.getsize(fileName)

s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_client.connect(address)
print(f'[>>] Connected to Server: {address}')

info = fileName + ':' + str(fileSize)
s_client.send(info.encode())
sleep(0.2)

with open(fileName, 'rb') as f:
    while True:
        read = f.read(2048)
        if not read:
            print('[=== File is uploaded ===]')
            break
        s_client.sendall(read)

s_client.close()