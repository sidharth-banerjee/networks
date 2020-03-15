'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import sys
from socket import *

serverName = sys.argv[1]
serverPort = 12000
filename = 'index.html'

if len(sys.argv) is 3:
    if 'html' in sys.argv[2]:
        filename = sys.argv[2]
    else:
        serverPort = int(sys.argv[2])

elif len(sys.argv) is 4:
    serverPort = int(sys.argv[2])
    filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = 'GET /' + filename + ' HTTP/1.1\n\r'
header1 = 'TE: deflate,gzip;q=0.3\n\r'
header2 = 'Connection: TE, closeHost: ' + serverName + ':' + str(serverPort)+ '\n\r'
header3 = 'User-Agent: lwp-request/6.39 libwww-perl/6.39\n\r\r'

message = request+header1+header2+header3
clientSocket.send(message.encode())


reply = clientSocket.recv(1024)
print(reply.decode())