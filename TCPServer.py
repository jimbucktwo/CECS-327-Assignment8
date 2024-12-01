import socket
import random
from pymongo import MongoClient


TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)
port = random.randint(1024, 49151)

TCPSocket.bind((IPaddress, port)) 
TCPSocket.listen(5)
print(f"IP address of server : {IPaddress}\nPort Number : {port}\nServer listening...")

incomingSocket, incomingAdress = TCPSocket.accept()
username = "jimmytraann"
password = "hpBSlmHHHj21lO3f"

uri = f"mongodb+srv://{username}:{password}@cluster0.4pkfm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client = MongoClient(uri)
    # Access the specific database

    # Test the connection
    print("Connected to MongoDB!")
    
except Exception as e:
    print(f"An error occurred: {e}")

def get_fridge2data(collection):
    data = collection["RealTimeData_virtual"]
    fridge2data = data.find({"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"})
    average_moisture = 0
    for i in fridge2data:
        moisture = i.get("payload", {}).get("Moisture Meter - fridge2sensor")
        if moisture:
            average_moisture += float(moisture)
    average_moisture /= len(list(fridge2data))
    print("Average Moisture: ", average_moisture)
    return None


while True:
    myData = incomingSocket.recv(1024).decode()
    collection = client["test"]

    #Change the following code to process the data received from the client
    if myData == '1':
        #Process average moisture inside the kitchen fridge in the past three hours
        get_fridge2data(client["test"])
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
client.close()