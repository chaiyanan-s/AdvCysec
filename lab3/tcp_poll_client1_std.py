import sys
import socket

if len(sys.argv) == 2:
	SERVER_IP = sys.argv[1]
	SERVER_PORT = int(sys.argv[2])
else:
	SERVER_IP = '127.0.0.1'
	SERVER_PORT = 3333

address = (SERVER_IP, SERVER_PORT)

def viewer_mode():
	print('\n[=====] Viewer Mode [=====]\n')
	while True:
		res = s_client.recv(2048)
		if res:
			print(f'[ VIEWER ] Response from the server: {res.decode()}')
		else:
			break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_client:
	print(f'[*] TCP Client is creating socket for server {address}')
	s_client.connect(address)
	print(f'[**] Connected to Server')

	while True:
		msg = input('[>>>] Enter your message: ')
		if msg == 'quit' or msg == '':
			s_client.sendall(b'')
			break
		s_client.sendall(msg.encode())
		if msg == 'v':
			viewer_mode()
		res = s_client.recv(2048)
		print(f'[<<<] Response from the server: {res.decode()}')
