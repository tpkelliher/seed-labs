#!/usr/bin/python3

# Receive UDP packets each of max size 'max_rcv' on any interface, listening
# on port 'port'.  Display a received packets count and the contents of
# each received packet.
#
# Terminate the server using ctrl-c.

import socket

ip = ''
port = 8080
max_rcv = 1024
cnt = 0

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
skt.bind((ip, port))

while True:
    data = skt.recv(max_rcv)
    cnt += 1
    print('Received ' + str(cnt) + ': ' + data.decode('utf-8'))
