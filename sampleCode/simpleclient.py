import socket
from time import sleep

# Buffer size
BUFFER_SIZE = 1024

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET means that this socket Internet Protocol v4 addresses
                                                    #SOCK_DGRAM means this is a UDP scoket

# Server application IP address and port
server_address = '127.0.0.1'
server_port = 10001

# client_socket.bind(('', 0)) 
# # ('', 0) '' means use the lokal IP adress    ,    0 means select a random open port
# portOfThisSocket = client_socket.getsockname()[1] # returns the previously selected (random) port
# print(f'{portOfThisSocket = }')


# Message sent to server
message = 'Hi server!'

try:
    # Send data to server
    client_socket.sendto(message.encode(), (server_address, server_port))
    print('Sent to server: ', message)

    # Receive response from server
    print('Waiting for response...')
    data, server = client_socket.recvfrom(BUFFER_SIZE)
    print('Received message from server at:', server)
    print(f'response = ' + data.decode('UTF8'))

finally:
    client_socket.close()
    print('Socket closed')
sleep(10)
