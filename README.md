# TCP Communication - Server and Client

This project demonstrates the use of TCP sockets for communication between a server and a client. The server listens for connections and processes specific requests from the client, returning corresponding responses based on the data received.

## Overview

- **TCPServer.py**: This is the server-side script. It listens for incoming connections on a specified port and processes the data received from the client. The server responds with relevant information based on the client's request.
- **TCPClient.py**: This is the client-side script. It connects to the server by entering the server’s IP address and port. The client sends requests to the server and waits for the response.

## Features

- **Server**:
    - Listens on a random port between 1024 and 49151.
    - Accepts client connections and handles requests from the client.
    - Provides responses like:
        - Average moisture in the kitchen fridge.
        - Water consumption per cycle in the smart dishwasher.
        - Electricity consumption among IoT devices (e.g., refrigerators and a dishwasher).

- **Client**:
    - Allows the user to choose one of the options:
        1. Average moisture in the kitchen fridge (past three hours).
        2. Average water consumption per cycle in the dishwasher.
        3. Which device consumes the most electricity (refrigerators vs. dishwasher).
    - Sends the selected option to the server and prints the server’s response.

## Prerequisites

- Python 3.x
- Socket library (standard in Python, no installation required)

## Setup and Running Instructions

### 1. Running the Server (`TCPServer.py`)

1. **Run the server script**:
    - Open a terminal and navigate to the directory where `TCPServer.py` is located.
    - Run the following command:
      ```bash
      python TCPServer.py
      ```
    - The server will print the IP address and port it is listening on.

2. **Port Configuration**:
    - The server will automatically choose a random port between 1024 and 49151. If you want to specify a port, modify the `port` variable in the script.

### 2. Running the Client (`TCPClient.py`)

1. **Run the client script**:
    - Open a new terminal window and navigate to the directory where `TCPClient.py` is located.
    - Run the following command:
      ```bash
      python TCPClient.py
      ```

2. **Connect to the Server**:
    - Enter the server’s IP address and the port number the server is listening on (provided by the server output).
    - You will then be presented with the following options:
        - `1`: Average moisture in the kitchen fridge.
        - `2`: Water consumption per cycle in the dishwasher.
        - `3`: Electricity consumption among IoT devices.
    - Enter one of the options (1-3) to get a response from the server.
    - To exit the client, enter `0`.

### 3. Example Usage

**Server Output** (when running `TCPServer.py`):



IP address of server : 192.168.1.10 Port Number : 60000 Server listening...

arduino
Copy code

**Client Output** (when running `TCPClient.py`):
Enter IP address: 192.168.1.10 Enter port number: 60000

What is the average moisture inside my kitchen fridge in the past three hours?
What is the average water consumption per cycle in my smart dishwasher?
Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)? (Enter 1-3 and 0 to Exit): 1 Server Response: "1"
css
Copy code

### 4. Error Handling

- If the client enters an invalid IP address or port, it will prompt for re-entry until a valid connection is established.
- If the client enters an invalid option (other than 1-3 or 0), it will ask the user to input a valid number between 1 and 3.


