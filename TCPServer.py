import socket
import random
from pymongo import MongoClient
import time
import os
from dotenv import load_dotenv

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

load_dotenv()
#MongoDB connection
username = os.getenv('USERNAME_KEY')
password = os.getenv('PASSWORD')

#Connection string to connect to the database
uri = f"mongodb+srv://{username}:{password}@cluster0.4pkfm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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

def get_fridge2_moisture(collection):

    data = collection["RealTimeData_virtual"]
    #query to find the average moisture in the last three hours
    fridge2data = data.find({'$and': [{"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    copy = data.find({'$and': [{"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    average_moisture = 0
    count = len(list(fridge2data))
    for i in copy:
        moisture = i.get("payload", {}).get("Moisture Meter - fridge2sensor")
        if moisture:
            average_moisture += float(moisture)
    if count != 0:
        average_moisture /= count * (40/100)
    else:
        print("No data found in the last three hours")
    formatted_average_moisture = "{:.2f}".format(average_moisture)
    

    return formatted_average_moisture


def get_fridge2_electricity(collection):
    data = collection["RealTimeData_virtual"]

    #query to find the electricity consumption
    fridge2data_electricity = data.find({"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"})
    count = len(list(fridge2data_electricity))
    electricity_consumption = 0
    for i in copy_electricity:
        electricity = i.get("payload", {}).get("ammetersensor2")
        if electricity:
            electricity_consumption += float(electricity)
    
    
    electricity_consumption = round(electricity_consumption * 120 / 1000 / count, 2)
    
    return electricity_consumption


def get_fridge1_moisture(collection):
    data = collection["RealTimeData_virtual"]
    #query to find the average moisture in the last three hours
    fridge2data = data.find({'$and': [{"payload.parent_asset_uid" : "o7a-l21-84y-y5d"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    copy = data.find({'$and': [{"payload.parent_asset_uid" : "o7a-l21-84y-y5d"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    average_moisture = 0
    count = len(list(fridge2data))
    for i in copy:
        moisture = i.get("payload", {}).get("Moisture Meter - fridge1sensor")
        if moisture:
            average_moisture += float(moisture)
    if count != 0:
        average_moisture /= count * (40/100)
    else:
        print("No data found in the last three hours")
    formatted_average_moisture = "{:.2f}".format(average_moisture)
    

    return formatted_average_moisture


def get_fridge1_electricity(collection):
    data = collection["RealTimeData_virtual"]

    #query to find the electricity consumption
    fridge2data_electricity = data.find({"payload.parent_asset_uid" : "o7a-l21-84y-y5d"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "o7a-l21-84y-y5d"})
    count = len(list(fridge2data_electricity))
    electricity_consumption = 0
    for i in copy_electricity:
        electricity = i.get("payload", {}).get("ammeter sensor")
        if electricity:
            electricity_consumption += float(electricity)
    
    
    electricity_consumption = round(electricity_consumption * 120 / 1000 / count, 2)
    
    return electricity_consumption



def get_dishwasher_waterconsumption(collection):
    data = collection["RealTimeData_virtual"]
    #query to find the electricity consumption
    dishwasher_electricity = data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})
    count = len(list(data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})))

    #query to find water consumption
    water_consumption = 0
    for i in dishwasher_electricity:
        water = i.get("payload", {}).get("waterconsumptionsensor")
        if water:
            water_consumption += float(water)
    
    if count != 0:
        water_consumption = round(water_consumption/3.785/count, 2)
    
    return water_consumption


def get_dishwasher_electricity(collection):
    data = collection["RealTimeData_virtual"]
    #query to find the electricity consumption
    dishwasher_electricity = data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})
    count = len(list(data.find({"payload.parent_asset_uid" : "4122cbc6-a4da-4237-9880-37eaf5dbd2c2"})))

    electricity_consumption = 0
    for i in copy_electricity:
        electricity = i.get("payload", {}).get("ammetersensor3")
        if electricity:
            electricity_consumption += float(electricity)
    electricity_consumption = round(electricity_consumption * 120 / 1000 / count, 2)
    
    return electricity_consumption



while True:
    myData = incomingSocket.recv(1024).decode()
    collection = client["test"]

    #Change the following code to process the data received from the client
    if myData == '1':
        #Process average moisture inside the kitchen fridge in the past three hours
        fridge1_moisture = get_fridge1_moisture(collection)
        fridge2_moisture = get_fridge2_moisture(collection)
        myData = f"Fridge1: {fridge1_moisture}%, Fridge2: {fridge2_moisture}%"
        incomingSocket.sendall(myData.encode())

    elif myData == '2':
        #Process water consumption per cycle in my smart dishwasher
        dishwasher_water = get_dishwasher_waterconsumption(collection)
        myData = f"{dishwasher_water} gallons per cycle"
        incomingSocket.sendall(myData.encode())

    elif myData == '3':
        #process electricity consumption among the IoT devices
        fridge1_electricity = get_fridge1_electricity(collection)
        fridge2_electricity = get_fridge2_electricity(collection)
        dishwasher_electricity = get_dishwasher_electricity(collection)

        if fridge1_electricity > fridge2_electricity and fridge1_electricity > dishwasher_electricity:
            myData = f"Fridge1 consumed more electricity: {fridge1_electricity} kWh per load"
        elif fridge2_electricity > fridge1_electricity and fridge2_electricity > dishwasher_electricity:
            myData = f"Fridge2 consumed more electricity: {fridge2_electricity} kWh per load"
        else:
            myData = f"Dishwasher consumed more electricity: {dishwasher_electricity} kWh per load"
            
        incomingSocket.sendall(myData.encode())

    else:
        print("Done")
        break

incomingSocket.close()
client.close()