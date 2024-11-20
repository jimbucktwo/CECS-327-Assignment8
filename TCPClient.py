import socket

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        serverIP = str(input("Enter IP address: "))
        serverPort = int(input("Enter port number: "))
        TCPSocket.connect((serverIP, serverPort))
        break
    except:
        print("Either the IP address or port number was entered incorrectly, try again.")


while True:
    message = input("Enter message you want to send (Enter to exit): ")
    if message:
        TCPSocket.sendall(message.encode())
        serverResponse = TCPSocket.recv(1024)
        print(f'Server Response: "{serverResponse.decode()}"')
    else:
        break


TCPSocket.close()