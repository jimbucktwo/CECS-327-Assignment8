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
    message = input("\n\n1. What is the average moisture inside my kitchen fridge in the past three hours?\n2. What is the average water consumption per cycle in my smart dishwasher?\n3. Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?\n(Enter 1-3 and 0 to Exit): ")
    if message == '1' or message == '2' or message == '3':
        TCPSocket.sendall(message.encode())
        serverResponse = TCPSocket.recv(1024)
        print(f'\n\n{serverResponse.decode()}')
    elif message == '0':
        break
    else:
        print("Invalid input. Please enter a number between 1 and 3.")


TCPSocket.close()