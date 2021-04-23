"""
Here are all the sockets.
There shall not be any sockets outside of this file.

There shall be one socket in one seperate thread (multithreading)
for every tcp connections
also one socket in a thread for the udp socket for broadcast
"""

import threading
import socket
import ipaddress



class Middleware():
    holdBackQueue = []
    deliveryQueue = []
        
    def __init__(self):
        pass

    def broadcast(ip, port, broadcast_message):
        # Create a UDP socket
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send message on broadcast address
        broadcast_socket.sendto(str.encode(broadcast_message), (ip, port))
        broadcast_socket.close()

    def broadcastToAll(self, message):
        SUBNETMASK = "255.255.255.0"
        BROADCAST_PORT = 61425
        SUBNETMASK = ipaddress.netmask.netmask
        IP_ADRESS_OF_THIS_PC = socket.gethostbyname(socket.gethostname())
        net = ipaddress.IPv4Network(IP_ADRESS_OF_THIS_PC + '/' + SUBNETMASK, False)
        BROADCAST_IP = net.broadcast_address.exploded

        # Send broadcast message
        message = IP_ADRESS_OF_THIS_PC + ' sent a broadcast'
        broadcast(BROADCAST_IP, BROADCAST_PORT, message)
        
    

    def sendMessageTo(self, uuid, message):
        pass



pass