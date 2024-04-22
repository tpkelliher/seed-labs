#!/usr/bin/python3

# Send 'count' UDP packets to the host with ip address 'ip' using port 'port'.

import socket

count = 12
ip = '10.9.0.11'
port = 8080

for i in range(count):
    print('Sending packet ' + str(i))
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.sendto(str.encode('packet ' + str(i) + '\n'), (ip, port))
    skt.close()
