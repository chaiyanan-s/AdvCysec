import socket, select

SERVER_IP = '0.0.0.0'
SERVER_PORT = 3333

address = (SERVER_IP, SERVER_PORT)

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print(f'[*] TCP Server is creating socket ... ({SERVER_IP}):{SERVER_PORT}')
s1.setblocking(False)
print(f'[**] Non-blocking mode is enabled')

s1.bind(address)
s1.listen(10)
print(f'[***] Listening for client (max: 10) at {s1.getsockname()}')

socks_dict = {s1.fileno(): s1}
addr_dict = {}
viewer_fd = []

# Correct constants
READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

poller = select.poll()
poller.register(s1, READ_ONLY)

while True:
    events = poller.poll()
    for fd, event in events:
        sock = socks_dict[fd]

        if event & (select.POLLIN | select.POLLPRI):
            if sock is s1:
                s_client, address = sock.accept()
                print('===================')
                print(f'[++] Accepted a new connection from: {s_client.getpeername()}')
                print(f'[++] Socket FD is : {s_client.fileno()}')
                print('===================')
                poller.register(s_client, READ_ONLY)
                socks_dict[s_client.fileno()] = s_client
                addr_dict[s_client] = address
            else:
                msg = sock.recv(2048)
                if msg:
                    msg = msg.decode()
                    print(f'[<<] Receiving message: {msg} from {addr_dict[sock]} (PC{fd-3})')
                    if msg.endswith('?'):
                        poller.modify(sock, READ_WRITE)
                    if msg == 'v':
                        viewer_fd.append(fd)
                    else:
                        msg = msg.upper()
                        sock.sendall(msg.encode())
                        print(f'[>>] Sending message: {msg} to {addr_dict[sock]} (PC{fd-3})')
                        for i in viewer_fd:
                            sock = socks_dict[i]
                            sock.sendall(msg.encode())
                            print(f'[ TO VIEWER ] Sending message: {msg} to {addr_dict[sock]}')
                else:
                    print('#############################')
                    print(f'Client {addr_dict[sock]} closed socket normally')
                    poller.unregister(sock)
                    del addr_dict[sock]
                    del socks_dict[fd]
                    print(f'addr_dict: {addr_dict.values()}')
                    print(f'socks_dict: {socks_dict.keys()}')
                    print('#############################')
                    sock.close()
        elif event & select.POLLOUT:
            msg = '=== Socket FD is ' + str(sock.fileno())
            sock.sendall(msg.encode())
            poller.modify(sock, READ_ONLY)