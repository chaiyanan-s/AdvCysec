import sys
import socket

if len(sys.argv) > 2:
    SERVER_IP = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])
else:
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 1111

address = (SERVER_IP, SERVER_PORT)
print(f'Server IP address: {address}')

# Create a TCP socket
clie_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'[*] TCP Client is creating socket for server {SERVER_IP}:{SERVER_PORT}')

# Connect to the server
clie_s.connect(address)
print('[*] Connected to server.')

while True:
    msg = input('[>>>] Enter your message: ')
    if msg == 'quit':
        clie_s.sendall(b'')  # Send an empty byte stream to signal end
        break
    clie_s.sendall(msg.encode())  # Send message to server

    # Receive response from server
    res = clie_s.recvfrom(2048)
    if not res:
        break
    print(f'[<<<] Response from the server: {res.decode()}')

clie_s.close()
