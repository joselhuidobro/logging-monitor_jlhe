#Range of applications/modules that publish logging information on the network.

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

#---- Getting Data from JSON file--------------------
      
with open('mssgs.json') as json_file:
 mssgs=json.load(json_file) 

#---- Send JSON data to client using socket ---------
while True:
    socket.send_json(mssgs)
    msg = socket.recv()
    print (msg)
    time.sleep(1)