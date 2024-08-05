import socket
import sys
import os

SERVER_IP = '0.0.0.0'
SERVER_PORT = 2222
fam_name = socket.AF_INET



s1 = socket.socket(fam_name, socket.SOCK_STREAM)
print(f'[*] TCP Server is creating socket ... ({SERVER_IP}):{SERVER_PORT}')

s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
print(f'[**] SO_REUSEADDR flag is used')
s1.bind((SERVER_IP,SERVER_PORT))
print(f'[***] Binding socket to local address')

s1.listen(1)
print(f'[****] Listening for client (max: 1) at {s1.getsockname()}')

s2, addr = s1.accept()
print(f'[<<<<] accept connection from {s2.getpeername()}')


file_info = s2.recv(2048).decode()
fileName, fileSize = file_info.split(':')

fileName = os.path.basename('new' + fileName)
fileSize = int(fileSize)

print(f'File Name: {fileName}')
print(f'File Size: {fileSize/1024:.2f} KB')

with open(fileName, 'wb') as f:
    while True:
        read = s2.recv(2048)
        if not read:
            break
        f.write(read)

s2.close()
s1.close()