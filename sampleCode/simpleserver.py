import socket
from time import sleep

# Buffer size
BUFFER_SIZE = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET means that this socket Internet Protocol v4 addresses
                                                    #SOCK_DGRAM means this is a UDP scoket

# Server application IP address and port
server_address = '127.0.0.1'
server_port = 10001

# Message to be sent to client
message = 'Hi client! Nice to connect with you!'

# Bind socket to port
server_socket.bind((server_address, server_port))
print('Server up and running at {}:{}'.format(server_address, server_port))

while True:
    print('\nWaiting to receive message...\n')
    sleep(100/1_000_000) #100 us
    
    # Receive message from client
    data, address = server_socket.recvfrom(BUFFER_SIZE)
    print('Received message from client: ', address)
    print('Message: ', data.decode())
    
    if data:
        # Send message to client
        server_socket.sendto(str.encode(message), address)
        print('Replied to client: ', message)
