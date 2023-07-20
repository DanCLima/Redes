from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client connected:", addr)

    while True:
        sentence = connectionSocket.recv(1024).decode("UTF-8")

        if not sentence:
            break

        if sentence == "ls":
            sentence = os.listdir()  # Obtém uma lista de nomes de todos os arquivos e diretórios
            modifiedSentence = "\n".join(sentence).encode("UTF-8")  # Transforma a lista de nomes de arquivos em uma única string separada por quebra de linhas
        elif sentence == "pwd":
            modifiedSentence = os.getcwd().encode("UTF-8")
        elif sentence.startswith("cd "):
            caminho = sentence[3:]  # Retira os 3 caracteres iniciais da string
            try:
                os.chdir(caminho)  # Acessando o diretório
                modifiedSentence = ("Diretório alterado para: " + os.getcwd()).encode("UTF-8")
            except FileNotFoundError:
                modifiedSentence = "Caminho inválido ou diretório não encontrado.".encode("UTF-8")
        else:
            modifiedSentence = "Comando inválido.".encode("UTF-8")

        connectionSocket.send(modifiedSentence)

    print("Client disconnected:", addr)
    connectionSocket.close()