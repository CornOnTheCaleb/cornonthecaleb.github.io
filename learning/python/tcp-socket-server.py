#!/usr/bin/env python3

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverHost = "localhost"
serverPort = 1234
serverSocket.bind((serverHost, serverPort))
serverMaxConnections = 1
serverSocket.listen(serverMaxConnections)

serverShouldTerminate = False
while not serverShouldTerminate:
  try:
    connectionSocket, clientAddress = serverSocket.accept()
    connectionSocket.settimeout(10)
    
    connectionShouldTerminate = False
    while not connectionShouldTerminate:
      try:
        maxBytesToReceive = 2048
        messageFromClient = connectionSocket.recv(maxBytesToReceive).decode()
        connectionSocket.send(messageFromClient.encode())
      except socket.timeout:
        connectionSocket.close()
        connectionShouldTerminate = True
  except KeyboardInterrupt:
    serverShouldTerminate = True

serverSocket.close()
