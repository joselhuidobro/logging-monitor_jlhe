#Range of applications/modules that publish logging information on the network.

#Currently, the logging can be viewed if needed, but is not monitored in any meaningful way.
#Focus on the implementation and not on the meaning/content of the data).
#Your challenge:

#Your task is to add a logging monitor to this setup, that continuously monitors the
#application logs for errors and/or patterns known to be problematic.

#The example code will publish JSON messages like the following:

import json
import zmq 
import time

print(zmq.pyzmq_version())

#-----ZeroMQ Server Setup---------

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:%s" % port)

#---- Getting Data from JSON file-------
# JSON string to converts it into a dictionary.
with open('mssgs.json') as json_file:
 mssgs=json.load(json_file) 

print(type(mssgs))
 

#---- send JSON data to client msg to client

while True:
    socket.send_json(mssgs)
    msg = socket.recv()
    print (msg)
    time.sleep(1)