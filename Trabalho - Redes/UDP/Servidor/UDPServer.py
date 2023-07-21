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
        elif message.startswith("scp "):
                nome_arq = message[4:]
                if os.path.exists(nome_arq):
                        # Enviando o nome do arquivo
                        modifiedMessage = nome_arq.encode("UTF-8") 
                        serverSocket.sendto(modifiedMessage, clientAddress)
                        
                        # Enviando o tamanho do arquivo
                        tam_arquivo = os.path.getsize(nome_arq)
                        modifiedMessage = str(tam_arquivo).encode("UTF-8")      # Transformando em string antes de codificar
                        serverSocket.sendto(modifiedMessage, clientAddress)

                        # Abre o arquivo como leitura
                        with open(nome_arq, 'rb') as file:
                                while tam_arquivo > 0:
                                        tam_buffer = 1024 if tam_arquivo >= 1024 else tam_arquivo

                                        # Lê os dados do arquivo
                                        dados = file.read(tam_buffer)
                                        tam_arquivo -= len(dados)

                                        # Envia os dados para o client
                                        serverSocket.sendto(dados, clientAddress)

                                        # Recebe a confirmação de recebimento do ACK
                                        serverSocket.recvfrom(1024)
                        
                        # Aguarda o próximo comando ou fechamento da conexão
                        continue
                else:
                        modifiedMessage = "null".encode("UTF-8")
        else:
                break
        serverSocket.sendto(modifiedMessage, clientAddress)