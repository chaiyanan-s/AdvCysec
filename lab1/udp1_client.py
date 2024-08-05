import sys
import socket

if len(sys.argv) > 2:
    SERVER_IP = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])
else:
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 1111

address = (SERVER_IP,SERVER_PORT)
print(f'Server IP address: {address}')

clie_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f'[*] UDP Client is creating socket for server {SERVER_IP}:{SERVER_PORT}')


while True:
    msg = input('[>>>] Enter your message: ')
    if msg == 'quit':
        clie_s.sendto(b'', address)
        break
    clie_s.sendto(msg.encode(), address)
    res, addr = clie_s.recvfrom(2048)
    print(f'[<<<] Response from the server: {res.decode()}:{addr}')

clie_s.close()