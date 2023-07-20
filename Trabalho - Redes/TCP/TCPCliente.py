from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode("UTF-8"))
modifiedSentence = clientSocket.recv(1024).decode("UTF-8")

print("From Server: ", modifiedSentence)
clientSocket.close()