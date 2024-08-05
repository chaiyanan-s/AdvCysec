import socket

import re
import ssl
 
# Define the UDP IP address and port to listen on
UDP_IP = "127.0.0.1"
UDP_PORT = 1111
 
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")
 
def decrypt_message(message):
    return ssl.PEM_cert_to_DER_cert(message).decode()

while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)
    data = decrypt_message(data.decode())
    print(f"Received packet from {addr}: {data}")