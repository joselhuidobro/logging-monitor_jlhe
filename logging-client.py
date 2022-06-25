from sqlite3 import Timestamp
import zmq
import time
import logging
import json

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

logger = logging.getLogger('__name__')#'__name__'
logging.basicConfig( filename="monitor.log",  format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger.debug('Client - Started')
logger.info('Server must be started before running this script')

def recieved():
    msg = socket.recv()
    socket.send_string("JSON data recieved from client")
    time.sleep(1)
    return(msg)

def log_function(module,timestamp,state,log_stream,log_message):
    
    logger.info("Message data:({0},{1},{2},{3},{4})".format(module,timestamp,state,log_stream,log_message))  
 
if __name__ == '__main__':
 
    try:
       while True:
         data = recieved()
         json_object = json.loads(data)
         #json object to list
         dict=json_object['messages']
         #print(dict,type(dict))
         #print(dict[1])
         for i in range(0,len(dict)):
            print(dict[0])
            #move in the dictionary
            a=dict[i]   
            #give a variable to each data field of the JSON file 
            module=a['module']
            timestamp=a['timestamp']
            state=a['state']
            log_stream=a['log-stream']
            log_message=a['log-message']
            #print to test
            print("module:", module)
            print("state:", state)
            print("timestamp:", timestamp)
            #send JSON values that now are STRINGS to the log function
            log_func=log_function(module,timestamp,state,log_stream,log_message)
                 
      
    except Exception as e:
         logging.exception("Exception occurred")
  
