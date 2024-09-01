from socket import *
serverName = gethostname()
serverPort = 9955
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('StudentID:')
clientSocket.send(message.encode())
responce = clientSocket.recv(1024)
print (responce.decode())
clientSocket.close()