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
    if myData:
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    else:
        print("Done")
        break

incomingSocket.close()