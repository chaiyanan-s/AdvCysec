import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 2024

family = socket.AF_INET
type = socket.SOCK_DGRAM
address = (SERVER_IP,SERVER_PORT)

client_socket = socket.socket(family,type)
print(f'[*] UDP client is creating socket for server {SERVER_IP}:{SERVER_PORT}')

def TCP(SERVER_PORT, addr):

    SERVER_IP = addr[0]
    SERVER_PORT = SERVER_PORT

    family = socket.AF_INET
    type = socket.SOCK_STREAM
    address = (SERVER_IP,SERVER_PORT)

    tcp_client_socket = socket.socket(family, type)
    print(f'[*] TCP Client is creating socket for server {address}')
    print(f'[**] Connected to Server')
    tcp_client_socket.connect(address)

    while True:
        msg = input('[TCP] Enter your message: ')
        if msg == 'quit':
            tcp_client_socket.sendall(b'')
            break
        tcp_client_socket.sendall(msg.encode())


while True:
    msg = input('[UDP] Input your message: ')
    if msg == 'quit':
        client_socket.sendto(b'', address)
        break
    client_socket.sendto(msg.encode(), address)

    res, addr = client_socket.recvfrom(2048)
    res = res.decode()

    if res.isdigit() and (int(res) >= 1024 and int(res) <= 65535):
        TCP(int(res), addr)

client_socket.close()