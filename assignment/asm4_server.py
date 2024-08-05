import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 2024

family = socket.AF_INET
type = socket.SOCK_DGRAM
address = (SERVER_IP,SERVER_PORT)

server_socket = socket.socket(family, type)
print(f'[*] UDP Server is creating socket ... {SERVER_IP}:{SERVER_PORT}')

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
print(f'[**] SO_REUSEADDR flag is used')
server_socket.bind(address)
print(server_socket)


def TCP(SERVER_PORT, addr, udp_server_socket):

    udp_server_socket.sendto(str(SERVER_PORT).encode(),addr)

    print(f'[<<<] Receiving reqested port: {SERVER_PORT} from {addr}')

    SERVER_IP = addr[0]
    SERVER_PORT = SERVER_PORT

    family = socket.AF_INET
    type = socket.SOCK_STREAM
    address = (SERVER_IP,SERVER_PORT)

    tcp_server_socket = socket.socket(family,type)
    tcp_server_socket.bind(address)
    print(tcp_server_socket)

    tcp_server_socket.listen(1)
    print(f'[*] Listening for client (max: 1) at {server_socket.getsockname()}')

    tcp_server_socket_2, addr_2 = tcp_server_socket.accept()
    print(f'[**] New port is created: {SERVER_PORT}')
    print(f'[****] Accept a connection from {tcp_server_socket_2.getpeername()}')

    while True:
        msg = tcp_server_socket_2.recv(2048)
        if not msg:
            print(f'QUIT signal from: {addr_2[0]}')
            break
        msg = msg.decode()
        print(f'[TCP] Receiving message: {msg} from {addr_2}')
    tcp_server_socket.close()
    tcp_server_socket_2.close()
    

while True:
    msg, addr = server_socket.recvfrom(2048)
    if not msg:
        print(f'QUIT signal from {addr[0]}')
        break
    msg = msg.decode()

    if msg.isdigit() and (int(msg) >= 1024 and int(msg) <= 65535):
        msg = int(msg)
        TCP(msg, addr, server_socket)
    else:
        print(f'[UDP] Receiving message: {msg} from {addr}')
        server_socket.sendto(str(msg).encode(),addr)

server_socket.close()
