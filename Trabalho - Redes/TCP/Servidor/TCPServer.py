from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode("UTF-8")

    if not sentence:
        break

    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode("UTF-8"))

    connectionSocket.close()