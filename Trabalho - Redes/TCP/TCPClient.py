import os
from socket import *

serverName = 'localhost'  
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:
    comando = input("Insira um comando: \n")
    if comando == "ls":
        clientSocket.send(comando.encode("UTF-8"))
        modifiedMessage = clientSocket.recv(2048).decode("UTF-8")
        print(modifiedMessage)
    elif comando == "pwd":
        clientSocket.send(comando.encode("UTF-8"))
        modifiedMessage = clientSocket.recv(2048).decode("UTF-8")
        print(modifiedMessage)
    elif comando.startswith("cd "):  # Verifica se o início da minha string contém "cd "
        clientSocket.send(comando.encode("UTF-8"))
        modifiedMessage = clientSocket.recv(2048).decode("UTF-8")
        print(modifiedMessage)
    elif comando.startswith("scp "):
        clientSocket.send(comando.encode("UTF-8"))
        modifiedMessage = clientSocket.recv(2048)
        if modifiedMessage.decode("UTF-8") == "null":
            print("Arquivo não encontrado.")
        else:
            # Recebe o nome/caminho do arquivo
            caminho = modifiedMessage

            # os.path.join extrai o nome do arquivo a partir do caminho completo
            nome_arq = os.path.basename(caminho.decode("UTF-8"))
            print("Nome do arquivo: " + nome_arq)

            # Recebe o tamanho do arquivo
            modifiedMessage = clientSocket.recv(2048)
            tam_arquivo = modifiedMessage.decode("UTF-8")
            tam_arquivo = int(tam_arquivo)  # Convertendo de string para inteiro
            print("Tamanho do arquivo: ", tam_arquivo)

            with open(nome_arq, 'wb') as file:
                while tam_arquivo > 0:
                    tam_buffer = 1024 if tam_arquivo >= 1024 else tam_arquivo

                    # Busca os dados do arquivo
                    dados = clientSocket.recv(tam_buffer)

                    # Escreve no arquivo
                    file.write(dados)
                    tam_arquivo -= len(dados)

                    # Envia a confirmação de recebimento ao servidor
                    clientSocket.send("ACK".encode("UTF-8"))
            print(f"Arquivo '{nome_arq}' baixado.")
    else:
        break
clientSocket.close()