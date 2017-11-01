#!/usr/bin/env python3

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverHost = "localhost"
serverPort = 1234
clientSocket.connect((serverHost, serverPort))

clientShouldTerminate = False
while not clientShouldTerminate:
  try:
    messageToSend = input("Message for server: ")
    clientSocket.send(messageToSend.encode())
    maxBytesToReceive = 2048
    messageFromServer = clientSocket.recv(maxBytesToReceive)
    print("Message from server:", messageFromServer)
  except KeyboardInterrupt:
    clientShouldTerminate = True

clientSocket.close()
