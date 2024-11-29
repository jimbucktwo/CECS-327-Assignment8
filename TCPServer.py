import socket
import random


TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)
port = random.randint(1024, 49151)

TCPSocket.bind((IPaddress, port)) 
TCPSocket.listen(5)
print(f"IP address of server : {IPaddress}\nPort Number : {port}\nServer listening...")

incomingSocket, incomingAdress = TCPSocket.accept()

while True:
    myData = incomingSocket.recv(1024).decode()

    #Change the following code to process the data received from the client
    if myData == '1':
        #Process average moisture inside the kitchen fridge in the past three hours
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    elif myData == '2':
        #Process water consumption per cycle in my smart dishwasher
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    elif myData == '3':
        #process electricity consumption among the IoT devices
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    else:
        print("Done")
        break

incomingSocket.close()