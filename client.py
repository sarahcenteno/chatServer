#!/usr/bin/env python3

import socket

# Connects to the local host with the following port
host = 'localhost'
port = 5713

# Creates TCP socket for server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))  # connects to the given host and port
message = input('Sending: ')  # asks user for an input
while True:  # loops until server sends back response to Thank you.
    clientSocket.send(message.encode())  # encodes and sends message from client to server
    modifiedMessage = clientSocket.recv(1024)  # receives encoded message from server
    print('From Server: ' + str(modifiedMessage.decode()))  # prints decoded message from server
    if modifiedMessage == "You are welcome. Have a nice day!":  # exit message
        print("Closing connection now...")
        break
    else:  # if no exit message, continues program
        message = input('Sending: ')
clientSocket.close()  # closes the socket
