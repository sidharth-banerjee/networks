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

request = 'GET http://' + serverName + ':' + str(serverPort) + '/' + filename 
print(request)
clientSocket.send(request.encode())


modifiedSentence = clientSocket.recv(1024)
print (modifiedSentence.decode())

clientSocket.close()