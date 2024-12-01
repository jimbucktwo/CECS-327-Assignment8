from pymongo import MongoClient
import time

three_hours_ago = int(time.time()) - 10800
lifespan_in_hours = int(time.time()) - 1731460517 / 3600

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
    #query to find the average moisture in the last three hours
    fridge2data = data.find({'$and': [{"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    copy = data.find({'$and': [{"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"}, {"payload.timestamp" : {"$gte" : f"{three_hours_ago}"}}]})
    average_moisture = 0
    count = len(list(fridge2data))
    for i in copy:
        moisture = i.get("payload", {}).get("Moisture Meter - fridge2sensor")
        if moisture:
            average_moisture += float(moisture)
    average_moisture /= count * (40/100)
    formatted_average_moisture = "{:.2f}".format(average_moisture)
    print("Average Moisture: ", formatted_average_moisture, "%")

    #query to find the electricity consumption
    fridge2data_electricity = data.find({"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "b7b24d10-bd59-4178-a3bc-61a4b0c63be5"})
    count = len(list(fridge2data_electricity))
    electricity_consumption = 0
    for i in copy_electricity:
        electricity = i.get("payload", {}).get("ammetersensor2")
        if electricity:
            electricity_consumption += float(electricity)
    
    
    electricity_consumption = round(electricity_consumption * 120 / 1000, 2)
    print("Electricity Consumption: ", electricity_consumption, "kWh")
    return [average_moisture, electricity_consumption]




def get_fridge1data(collection):
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
    average_moisture /= count * (40/100)
    formatted_average_moisture = "{:.2f}".format(average_moisture)
    print("Average Moisture: ", formatted_average_moisture, "%")

    #query to find the electricity consumption
    fridge2data_electricity = data.find({"payload.parent_asset_uid" : "o7a-l21-84y-y5d"})
    copy_electricity = data.find({"payload.parent_asset_uid" : "o7a-l21-84y-y5d"})
    count = len(list(fridge2data_electricity))
    electricity_consumption = 0
    for i in copy_electricity:
        electricity = i.get("payload", {}).get("ammeter sensor")
        if electricity:
            electricity_consumption += float(electricity)
    
    
    electricity_consumption = round(electricity_consumption * 120 / 1000, 2)
    print("Electricity Consumption: ", electricity_consumption, "kWh")
    return [average_moisture, electricity_consumption]

get_fridge1data(client["test"])