import os

from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
comando = 1

while 1:
    comando = input("Insira um comando: ")
    if comando == "upper":
        message = input('Input lowercase sentence: ')
        clientSocket.sendto(message.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    elif comando == "ls":
        clientSocket.sendto(comando.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    elif comando == "pwd":
        clientSocket.sendto(comando.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    elif comando.startswith("cd "):     # Verifica se o início da minha string contém "cd "
        clientSocket.sendto(comando.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode("UTF-8"))
    elif comando.startswith("scp "):
        clientSocket.sendto(comando.encode("UTF-8"),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        if modifiedMessage.decode("UTF-8") == "null":
            print("Arquivo não encontrado.")
        else:
            # Recebe o nome/caminho do arquivo
            caminho = modifiedMessage.decode("UTF-8")

            # os.path.join extrai o nome do arquivo a partir do caminho completo
            nome_arq = os.path.basename(caminho)
            print("Nome do arquivo: " + nome_arq)

            # Recebe o tamanho do arquivo
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            tam_arquivo = modifiedMessage.decode("UTF-8")
            tam_arquivo = int(tam_arquivo)  # Convertendo de string para inteiro
            print("Tamanho do arquivo: ", tam_arquivo)
        
            with open(nome_arq, 'wb') as file:
                while tam_arquivo > 0:
                    # Busca os dados do arquivo
                    byte, serverAddress = clientSocket.recvfrom(1)

                    # Escreve no arquivo
                    file.write(byte)
                    tam_arquivo -= 1
            print(f"Arquivo '{nome_arq}' baixado." )

            # COMANDO CLIENT: UDPClient.py
    else:
        break


clientSocket.close()

# Problemas
# Quando uso o scp e passo um caminho ele corrompe o arquivo (resolvido)
# Quando da scp e dps qlq outro comando dá problema (resolvido)
# Ao fazer um download de um arquivo com o msm nome ele fica corrompido