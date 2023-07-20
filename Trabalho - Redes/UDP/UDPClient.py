import os

from socket import *
serverName = 'localhost' # Usar 'localhost' se estiver na mesma máquina com windows ou o IP do servidor se estiver em 2 computadores
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while 1:
    comando = input("Insira um comando: \n")
    if comando == "ls":
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
                    tam_buffer = 1024 if tam_arquivo >= 1024 else tam_arquivo

                    # Busca os dados do arquivo
                    dados, serverAddress = clientSocket.recvfrom(tam_buffer)

                    # Escreve no arquivo
                    file.write(dados)
                    tam_arquivo -= len(dados)

                    # Envia a confirmação de recebimento ao servidor
                    clientSocket.sendto("ACK".encode("UTF-8"),(serverName, serverPort))
            print(f"Arquivo '{nome_arq}' baixado." )
    else:
        break
clientSocket.close()