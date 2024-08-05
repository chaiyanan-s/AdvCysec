import sys
import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 1111

address = (SERVER_IP, SERVER_PORT)
serv_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'[*] TCP Server is creating socket... {SERVER_IP}:{SERVER_PORT}')
serv_s.bind(address)
print(f'[**] Binding socket to local address {address}')

serv_s.listen(5)  # Allow the server to accept connections
print('[**] Server is listening for connections...')

while True:
    conn, addr = serv_s.accept()  # Accept a new connection
    print(f'[***] Connection established with {addr}')

    while True:
        msg = conn.recv(2048)  # Receive data from the client
        if not msg:
            print(f'Connection closed by {addr}')
            break
        msg = msg.decode()
        print(f'[<<<] Receiving message: {msg} from {addr}')
        msg = msg.upper()
        conn.sendall(msg.encode())  # Send data back to the client
        print(f'[>>>] Sending message: {msg} to {addr}')

    conn.close()  # Close the connection
