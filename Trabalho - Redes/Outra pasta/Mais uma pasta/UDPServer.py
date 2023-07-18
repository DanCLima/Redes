import os

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode("UTF-8")
        if message == "pwd":
                modifiedMessage = os.getcwd().encode("UTF-8")
        elif message == "ls":
                message = os.listdir()  # Obtem uma lista de nomes de todos os arquivos e diretórios
                modifiedMessage = "\n".join(message).encode("UTF-8")    # Transforma a lista de nomes de arquivos em uma única string separada por quebra de linhas
        elif message == "cd":
                modifiedMessage = os.getcwd().encode("UTF-8")
        serverSocket.sendto(modifiedMessage, clientAddress)




        # modifiedMessage = message.upper().encode("UTF-8")