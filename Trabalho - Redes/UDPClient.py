import os

from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
comando = 1

while 1:
    comando = input("Digite um comando válido: ")
    if comando == "upper":
        message = input('Input lowercase sentence: ')
        clientSocket.sendto(message.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    if comando == "pwd":
        clientSocket.sendto(comando.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    else:
        break


clientSocket.close()