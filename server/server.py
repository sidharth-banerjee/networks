'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import sys
import time
from threading import Thread
from socket import SOL_SOCKET, SO_REUSEADDR
from socket import socket, AF_INET, SOCK_STREAM

def returnFileData(filepath):
    if 'htm' not in filepath.decode():
        f = open('default.html')
        outputdata = f.read()
        f.close()

    else:
        f = open(filepath[1:])
        outputdata = f.read()
        f.close()

    return outputdata

class ClientThread(Thread):
    def __init__(self, connectionSocket, ip, port):
        Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.ip = ip
        self.port = port

    def run(self):
        try:
            message = self.connectionSocket.recv(1024)

            filename = message.split()[1]
            
            outputdata = returnFileData(filename)

            # send HTTP header line into socket
            self.connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
            
            for i in range (0, len(outputdata)):
                self.connectionSocket.send(outputdata[i].encode())

            print('\nRequest Details:\n')
            print(message.decode())
            print('File Sent at ' + time.ctime())
            print()
            self.connectionSocket.close()
            
        except IOError:
            self.connectionSocket.send('\nHTTP/1.1 404 Not Found\n'.encode())
            self.connectionSocket.close()


serverPort = 8080 # default
if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))

print('\nHTTP server is active on port ', serverPort)

while True:
    serverSocket.listen(5)
    (connectionSocket, (ip, port)) = serverSocket.accept()
    t = ClientThread(connectionSocket, ip, port)
    t.setDaemon(True)
    t.start()