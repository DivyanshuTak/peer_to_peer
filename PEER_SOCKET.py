import socket
import string
import _thread
import threading

#================================================================================================================
LISTEN_PORT = 60070
TALK_PORT = 60071
dummy=0
MAX_CONNECTIONS = 3
MESSAGE_SENT =0
MESSAGE_READY =0
PEER_IP_LIST = []
FINAL_IP_LIST = []
client_socket = socket.socket()
#===================================================================
#-------------------------------------------------------------------
#===============================================================================================================
#                              CLASS FOR MULTITHREADING
#----------------------------------------------------------------------------------------------------------------
class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        #print("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        local_dummy=0
        msg = 'ACKNOWLEDGE'
        self.csocket.send(bytes(msg, 'UTF-8'))
        while True:
            if MESSAGE_READY:
                HEADER = universal_string[:10]
                if HEADER == clientAddress:
                    self.csocket.send(bytes(universal_string, 'UTF-8'))
                    MESSAGE_READY =0

      #  while not SYNC_DONE:
      #     pass
      #  while local_dummy < MAX_CONNECTIONS:
      #      self.csocket.send(bytes(IP_LIST[local_dummy], 'UTF-8'))
      #      local_dummy = local_dummy + 1
        self.csocket.close()
        #while True:
         #   data = self.csocket.recv(2048)
          #  msg = data.decode()
           # if msg == 'bye':
            #    break
           # print("from client", msg)
           # self.csocket.send(bytes(msg, 'UTF-8'))
        #print("Client at ", clientAddress, " disconnected...")
#----------------------------------------------------------------------------------
#                         END OF CLASS
#----------------------------------------------------------------------------------
#            FUNCTION WITH AGRS(IP OF THE PEER) IS HERE
#*********************************************************************************

def peer_listen(ip_adress):
    'this is the base function for listning socket'
    listen_peer = socket.socket()
    listen_peer.connect((ip_adress,LISTEN_PORT))
    while True:
        recv_string = listen_peer.recv(4096)
        print(ip_adress +"sent::"+ recv_string)
        if recv_string == "b'BYE'":
            break
    listen_peer.close()


#===================================================================
#                  CLIENT INITIALISATION
#===================================================================
client_ip = socket.gethostname()
LOCAL_IP = socket.gethostbyname(client_ip)
port = 60069
print(client_ip)
client_socket.connect(("192.168.1.7",port))                                    # type the ip of the central server here
indicator = "your message :: "
#======================================================================
#                   ININTIALISATION COMPLETE
#======================================================================
#       GETTING THE COMPLETE IP LIST FROM THE CENTRAL SERVER
#======================================================================
print(client_socket.recv(1024))  # this is ACKNOWLEDGE
dummy = 0
try:
    while dummy < MAX_CONNECTIONS:
        PEER_IP_LIST.append(client_socket.recv(1024))
        dummy = dummy + 1
except:
    print("didnt got the ip list ")
print(PEER_IP_LIST)
client_socket.close()
 #----------------------------------------------------------------------------------------------------------------

 #-----------------------------------------------------------------------------------------------------------------
#======================================================================
#           COMPLETE PEER IP LIST HAS BEEN RECIEVED HERE
# NOW THERE IS NO NEED FOR CENTRAL SERVER SO CLOSE THE CONNECTION WITH IT
#   FILTER THE MACHINE IP AND OPEN THE CONNECTION FOR THE OTHETS
#======================================================================
dummy=0
for dummy in len(PEER_IP_LIST):
    if not (PEER_IP_LIST[dummy]==LOCAL_IP):
        FINAL_IP_LIST[dummy] = PEER_IP_LIST[dummy]


#===========================================================================
#                      FINAL IP LIST IS UPDATED
#============================================================================
#------------------     SET THE TALKING SOCKET    ---------------------------

talk_peer = socket.socket()
talk_peer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
talk_peer.bind((LOCAL_IP, TALK_PORT))
print("TALKING Server started")
dummy = 0
while dummy < (MAX_CONNECTIONS - 1) :
    talk_peer.listen(1)
    clientsock, clientAddress = talk_peer.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
    dummy = dummy + 1

print("all threads are running")
print("initialing the listning threads")

#-----------------     SET THE RECEIVEING SOCKET   ----------------------------

try:
    dummy_listen=0
    while dummy_listen < (MAX_CONNECTIONS - 1):
        _thread.start_new_thread(peer_listen,FINAL_IP_LIST[dummy_listen])
        dummy_listen = dummy_listen+1

except:
    print("failed to initialise the listning ports")


#----------------------------------------------------------------------------------
#                           ENTER THE MESSAGE HERE
#----------------------------------------------------------------------------------
print("\n")
print("================================================================")
print("ALL THE INITIALISATION IS COMPLETE HERE")
print("THE PEER TO PEER IS NOW ACTIVE ")
print("TO EXIT A PARTICULAR NETWORK TYPE << BYE >>")
print("=================================================================")

#----------------------------------------------------------------------------------
# ASSORT THE STRING ACCORDING TO PARTICULAR NETWORK AND SEND IT AUTOMATICALLY
#----------------------------------------------------------------------------------

while True:
    if not MESSAGE_READY:
        universal_string = input()
        MESSAGE_READY=1

print("end of the fucking programme")







































