import sys
import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 1111

address = (SERVER_IP,SERVER_PORT)
serv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f'[*] UDP Server is creating socket...{SERVER_IP}:{SERVER_PORT}')
serv_s.bind(address)
print(f'[**] Binding socket to local address {address}')

while True:
    msg, address = serv_s.recvfrom(2048)
    if not msg:
        print(f'QUIT signals form: {address[0]}')
    msg = msg.decode()
    print(f'[<<<] Receiving message: {type(msg)} from {address}')
    msg = msg.upper()
    serv_s.sendto(msg.encode(), address)
    print(f'[>>>] Sending message: {msg} to {address}')

serv_s.close()