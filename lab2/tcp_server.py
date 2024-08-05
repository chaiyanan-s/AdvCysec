import socket
import sys

SERVER_IP = '0.0.0.0'
SERVER_PORT = 2222
fam_name = socket.AF_INET

if len(sys.argv) > 1:
    if (sys.argv[1].lower() == 'ipv6') and socket.has_ipv6:
        SERVER_IP = '::'
        fam_name - socket.AF_INET6

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

print(s1)
print(s2)

while True:
    msg = s2.recv(2048)
    if not msg:
        print(f'QUIT signals from: {addr[0]}')
        break
    msg = msg.decode()
    print(f'[<<<] Receiving message: {msg} from {addr}')
    msg = msg.upper()
    s2.sendall(msg.encode())
    print(f'[>>>] Sending message: {msg} to {addr}')
s2.close()
s1.close()
