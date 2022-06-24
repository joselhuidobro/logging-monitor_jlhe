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
    
    logger.info("modulo es ({0}, {1}, {2}, {3} , {4})".format(module,timestamp,state,log_stream,log_message))
 
 
if __name__ == '__main__':
    #send JSON values to the log function
    log_func=log_function('a',2,3,4,5)
    try:
       while True:
         data = recieved()
         json_object = json.loads(data)
         dict=json_object['messages']
         print(dict,type(dict))
         print(dict[1])
         
        # print(json_object['messages']) 
       
         #print(json_object,type(json_object))
         
         
      
    except Exception as e:
         logging.exception("Exception occurred")
  
