import socket
import random
from pymongo import MongoClient
import time

#Initiates the socket and hostname
TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)
port = random.randint(1024, 49151)

#establishes the connection
TCPSocket.bind((IPaddress, port)) 
TCPSocket.listen(5)
print(f"IP address of server : {IPaddress}\nPort Number : {port}\nServer listening...")

incomingSocket, incomingAdress = TCPSocket.accept()


#MongoDB connection
username = "jimmytraann"
password = "hpBSlmHHHj21lO3f"

#Connection string to connect to the database
uri = f"mongodb+srv://{username}:{password}@cluster0.4pkfm.mongodb.net/Cluster0?retryWrites=true&w=majority"
print(uri)
try:
    client = MongoClient(uri)
    # Access the specific database

    # Test the connection
    print("Connected to MongoDB!")
    
except Exception as e:
    print(f"An error occurred: {e}")

#calculations for querying the database
three_hours_ago = int(time.time()) - 10800
lifespan_in_hours = int(time.time()) - 1731460517 / 3600

db = client["test"]
collection = db["RealTimeData_virtual"]

def get_fridge2_moisture():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': 'b7b24d10-bd59-4178-a3bc-61a4b0c63be5', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'average_moisture': {
                '$avg': {'$toDouble' : '$payload.Moisture Meter - fridge2sensor'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['average_moisture'] / 40  * 100:.2f}"
        
        return formatted


def get_fridge2_electricity():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': 'b7b24d10-bd59-4178-a3bc-61a4b0c63be5', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'electricity': {
                '$avg': {'$toDouble' : '$payload.ammetersensor2'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['electricity'] * 120 * 3/1000:.2f}"
        
        return formatted


def get_fridge1_moisture():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': 'o7a-l21-84y-y5d', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'average_moisture': {
                '$avg': {'$toDouble' : '$payload.Moisture Meter - fridge1sensor'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['average_moisture'] / 40  * 100:.2f}"
        
        return formatted


def get_fridge1_electricity():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': 'o7a-l21-84y-y5d', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'electricity': {
                '$avg': {'$toDouble' : '$payload.ammeter sensor'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['electricity'] * 120 * 3/1000:.2f}"
        
        return formatted



def get_dishwasher_waterconsumption():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': '4122cbc6-a4da-4237-9880-37eaf5dbd2c2', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'waterconsumption': {
                '$avg': {'$toDouble' : '$payload.waterconsumptionsensor'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['waterconsumption']:.2f}"
        
        return formatted


def get_dishwasher_electricity():
    result = collection.aggregate([
    {
        '$match': {
            'payload.parent_asset_uid': '4122cbc6-a4da-4237-9880-37eaf5dbd2c2', 
            'payload.timestamp': {
                '$gte': f'{three_hours_ago}'
            }
        },
        
    }, {
        '$group': {
            '_id': None, 
            'electricity': {
                '$avg': {'$toDouble' : '$payload.ammetersensor3'}
            }
        }
    }
    ])

    if not result:
        return "No data found in the last three hours"
    
    for i in result:
        formatted = f"{i['electricity'] * 120 * 3/1000:.2f}"
        
        return formatted



while True:
    myData = incomingSocket.recv(1024).decode()

    #Change the following code to process the data received from the client
    if myData == '1':
        #Process average moisture inside the kitchen fridge in the past three hours
        fridge1_moisture = get_fridge1_moisture()
        fridge2_moisture = get_fridge2_moisture()
        myData = f"Fridge1: {fridge1_moisture}%, Fridge2: {fridge2_moisture}%"
        print(myData)
        incomingSocket.sendall(myData.encode())

    elif myData == '2':
        #Process water consumption per cycle in my smart dishwasher
        dishwasher_water = get_dishwasher_waterconsumption()
        myData = f"{dishwasher_water} gallons per cycle"
        print(myData)
        incomingSocket.sendall(myData.encode())

    elif myData == '3':
        #process electricity consumption among the IoT devices
        fridge1_electricity = get_fridge1_electricity()
        fridge2_electricity = get_fridge2_electricity()
        dishwasher_electricity = get_dishwasher_electricity()

        if fridge1_electricity > fridge2_electricity and fridge1_electricity > dishwasher_electricity:
            myData = f"Fridge1 consumed more electricity: {fridge1_electricity} kWh per load"
        elif fridge2_electricity > fridge1_electricity and fridge2_electricity > dishwasher_electricity:
            myData = f"Fridge2 consumed more electricity: {fridge2_electricity} kWh per load"
        else:
            myData = f"Dishwasher consumed more electricity: {dishwasher_electricity} kWh per load"
        print(myData)
        incomingSocket.sendall(myData.encode())

    else:
        print("Done")
        break

incomingSocket.close()
client.close()