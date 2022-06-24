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
socket.bind("tcp://*:%s" % port)

#---- Getting Data from JSON file-------
mssgs = open('mssgs.json')
JSON_mssgs=mssgs
# returns a dictionary 
data = json.load(mssgs)
# Iterating through the list
for i in data["messages"]:
    print(i)
mssgs.close()

#---- send hello world msg to client

while True:
    socket.send_string('Hello Im server')
    msg = socket.recv()
    print (msg)
    time.sleep(1)