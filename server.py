#!/usr/bin/env python

import socket

host = ''
port = 5713

# Creates TCP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))  # server connects to given host and port
serverSocket.listen(2) # server listens for incoming TCP requests
print("Server started")
print("Waiting for client request...")
conn, addr = serverSocket.accept()  # server will accept new request
print("Connection from: " + str(addr))  # prints connected IP address
while True:  # loops until Thank you. message and then breaks and ends program
    message = conn.recv(1024).decode()  # decode message received from client
    print("From Client: " + str(message))  # prints message from client
    # if client sends any of the following messages, the server will send back
    # an encoded pre-determined message to the client and prints what it will
    # be sending to the client
    if message == "What is your name?":
        conn.send("My name is Sarah Centeno.".encode())
        print("Sending: My name is Sarah Centeno.")
    elif message == "What course is this project for?":
        conn.send("This project is for CNT4704, Fall 2019.".encode())
        print("Sending: This project is for CNT4704, Fall 2019.")
    elif message == "How many programming assignments do we have?":
        conn.send("I think there are two.".encode())
        print("Sending: I think there are two.")
    elif message == "Do you think the second part is more challenging?":
        conn.send("Of course, the first part (socket programming) has been done for you.".encode())
        print("Sending: Of course, the first part (socket programming) has been done for you.")
    elif message == "How do you know to respond to these questions?":
        conn.send("You programmed me, didn't you?".encode())
        print("Sending: You programmed me, didn't you?")
    elif message == "Can I ask you a personal question?":
        conn.send("I don't think you'd like the answer.".encode())
        print("Sending: I don't think you'd like the answer.")
    elif message == "Can you answer an arbitrary question?":
        conn.send("Yes, I can, but I won't".encode())
        print("Sending: Yes, I can, but I won't.")
    elif message == "Thank you.":
        conn.send("You are welcome. Have a nice day!".encode())
        print("Sending: You are welcome. Have a nice day!")
        print("Closing connection now...")
        break
    else:
        conn.send("I do not understand your question. Please re-enter your question.".encode())
        print("Sending: I do not understand your question. Please re-enter your question.")
    if not message:  # if message was not received, then it will break away from program
        break
conn.close()  # closes the connection

