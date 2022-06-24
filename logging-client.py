import zmq
import time
import logging

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)


def recieved():
    msg = socket.recv()
    socket.send_string("JSON data recieved from client")
    time.sleep(1)
    return(msg)


 


if __name__ == '__main__':
    logger = logging.getLogger()#'__name__'
    logging.basicConfig( filename="monitor.log",  format='%(asctime)s - %(message)s', level=logging.DEBUG)
  #  logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)
    
    logging.info('Client logged in')
    logging.warning('Server must be started before running this script')
    # Create handlers
    #stream_handler = logging.StreamHandler()
    #file_handler = logging.FileHandler('msg.log')

    #LEVELS
    #stream_handler.setLevel(logging.WARNING)
    #file_handler.setLevel(logging.ERROR)

    #FORMAT
 
    #file_format =logging.Formatter('%(asctime)s - %(message)s')

    #logger.addHandler(stream_handler)
    #logger.addHandler(file_handler)

   
    try:
       while True:
     #logger.warning('Protocol problem: %s', 'connection reset', extra=connect)
         data = recieved()
         print (data)
    except Exception as e:
         logging.exception("Exception occurred")
  
