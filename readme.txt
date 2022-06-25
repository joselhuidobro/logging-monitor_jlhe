Author: José Luis Huidobro Echeverría

-----------Logging Monitor Task-----------
 Please in a terminal RUN:
 
  python logging-server.python
 
 On another terminal RUN:
  
  python logging-client.python

The server is going to send messages to client,
 all events are saved on the monitor.log file

While both Scripts are running please open the monitor.log file to view events

script "logging-server.py"----------------------
- Creates a connection between server and client,
  setting up the host and port through a Socker using zmq.
- Reads the JSON data from the mssgs.json file.
- The server Sends the JSON data to the client.


Script "logging-client.py" ---------------------

- Script recieves the data through a Socket using zmq 
- Sends a message back to the server 
- Prints the recieved JSON data 
- Creates the file "monitor.log" where activity is being registered, also logs, warning,  


Requirements: pip install pyzmq-static