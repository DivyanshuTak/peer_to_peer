import socket
import os
import threading
import _thread
from socketserver import ThreadingMixIn
#======================================INITIALISE ALL THE VARIABLES===================================================
SYNC_BIT = 0
CENTRAL_IP = "0.0.0.0"
CLOSE_CONNECTION = 0
CLIENT_count = 0
TIMEOUT = 0
HOST_count = 0
flag_1 = 0
flag_2 = 0
flag_3 = 0
MAX_CONNECTIONS = 5
MIN_CONNECTIONS = 1
BASE_PORT = 60069
IP_1 = "0.0.0.0.0"
IP_2 = "0.0.0.0.0"
IP_3 = "0.0.0.0.0"
IP_4 = "0.0.0.0.0"
IP_5 = "0.0.0.0.0"
IP_LIST = []
ACTIVE_CONNECTIONS = 0
#=========================================GLOBAL VARIABLES ENDS HERE===================================================


CENTRAL_IP = "192.168.43.126"

def dummy_connections():
    dummy=0
    central_host = socket.socket()
    # =================================================================
    #                       ININTIALISE THE HOST
    # =================================================================
    try:
        central_host.bind((CENTRAL_IP, BASE_PORT))
        print("host is active")
    except:
        print("binding error")

    central_host.listen(5)
    client_1,addr = central_host.accept()
    new_thread = ClientThread(addr[0],addr[1])
    new_thread.start()
    client_1.send(b'ACKNOWLEDGE')
    IP_LIST.append(addr[0])
    #while not SYNC_BIT:
       # pass
    #for dummy in MAX_CONNECTIONS:
      #  client_1.send(bytes(IP_LIST[dummy] , 'utf-8'))
    #client_1.close()

try:
    _thread.start_new_thread(dummy_connections, ())
    _thread.start_new_thread(dummy_connections, ())
    _thread.start_new_thread(dummy_connections, ())
    _thread.start_new_thread(dummy_connections, ())
    _thread.start_new_thread(dummy_connections, ())
except:
    print("connection not possible")


#while(IP_LIST[5] == "0"):
 #   pass
#SYNC_BIT=1

while True:
    pass
    #print(IP_LIST)
    #print("\n")











