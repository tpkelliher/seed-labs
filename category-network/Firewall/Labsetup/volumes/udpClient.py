#!/usr/bin/python3

# Send 'count' UDP packets to the host with ip address 'ip' using port 'port'.
# Count is expected as a command line argument.  For example:
#
#     ./udpClient.py 42
#
# It is not standard practice to open a socket, send one packet, and then
# close it.  It is inefficient.  Doing so here ensures that each packet
# sent is sent individually.  Otherwise, multiple messages would be bundled
# into a single packet.

import socket
import sys

ip = '10.9.0.11'
port = 8080

if len(sys.argv) != 2:
    print('Expecting one numeric argument')
    exit(1)

try:
    count = int(sys.argv[1])
except:
    print('Expecting one numeric argument')
    exit(1)

print('Using count of ' + str(count))

for i in range(1, count + 1):
    print('Sending message ' + str(i))
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.sendto(str.encode('packet ' + str(i)), (ip, port))
    skt.close()
