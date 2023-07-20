from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    comando = input("Insira um comando: ")
    if comando == "ls":
        clientSocket.send(comando.encode("UTF-8"))
        modifiedSentence = clientSocket.recv(1024).decode("UTF-8")
        print (modifiedSentence)
    elif comando == "pwd":
        clientSocket.send(comando.encode("UTF-8"))
        modifiedSentence = clientSocket.recv(1024).decode("UTF-8")
        print (modifiedSentence)
    elif comando.startswith("cd "):     # Verifica se o início da minha string contém "cd "
        clientSocket.send(comando.encode("UTF-8"))
        modifiedSentence = clientSocket.recv(1024).decode("UTF-8")
        print (modifiedSentence)
    else:
        break

clientSocket.close()