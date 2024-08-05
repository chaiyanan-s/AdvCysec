import socket
import sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 2222
fam_name = socket.AF_INET

if len(sys.argv) > 2:
    if (sys.argv[1].lower() == 'ipv6') and socket.has_ipv6:
        SERVER_IP = sys.argv[2]
        fam_name = socket.AF_INET6
adderss = (SERVER_IP, SERVER_PORT)

s_client = socket.socket(fam_name, socket.SOCK_STREAM)
print(f'[*] TCP Client is creating socket for server {adderss}')
s_client.connect(adderss)
print(f'[**] Connected to Server')

while True:
    msg = input('[>>>] Enter your message: ')
    if msg == 'quit':
        s_client.sendall(b'')
        break
    s_client.sendall(msg.encode())
    res = s_client.recv(2048)
    print(f'[<<<] Response from server: {res.decode()}')
s_client.close()
