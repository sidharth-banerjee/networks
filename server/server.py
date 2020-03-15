import sys
import threading
from socket import *

def returnFileData(filepath):
    if 'html' not in filepath.decode():
        f = open('default.html')
        outputdata = f.read()
        f.close()

    else:
        f = open(filepath[1:])
        outputdata = f.read()
        f.close()

    return outputdata


serverPort = 12000 # default
if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('\nHTTP server is active on port ', serverPort)
print()

while 1:
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        outputdata = returnFileData(filename)

        # send HTTP header line into socket
        connectionSocket.send('\nHTTP/1.x 200 OK\n'.encode())

        for i in range (0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

        print('\nRequest Details:\n')
        print(message.decode().strip('\r\n'))
        print('File Sent\n')
    
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n'.encode())
        connectionSocket.close()
    
serverSocket.close()