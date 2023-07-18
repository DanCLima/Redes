import os

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode("UTF-8")
        
        if message == "ls":
                message = os.listdir()  # Obtem uma lista de nomes de todos os arquivos e diretórios
                modifiedMessage = "\n".join(message).encode("UTF-8")    # Transforma a lista de nomes de arquivos em uma única string separada por quebra de linhas
        elif message == "pwd":
                modifiedMessage = os.getcwd().encode("UTF-8")
        elif message.startswith("cd "):
                caminho = message[3:]   # Retira os 3 caracteres iniciais da string
                try:
                        os.chdir(caminho)       # Acessando o diretório
                        modifiedMessage = ("Diretório alterado para: " + os.getcwd()).encode("UTF-8")
                except FileNotFoundError:
                        modifiedMessage = "Caminho inválido ou diretório não encontrado.".encode("UTF-8")
        else:
                modifiedMessage = message.upper().encode("UTF-8")
        serverSocket.sendto(modifiedMessage, clientAddress)