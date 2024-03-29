import socket
import threading

SYNC_DONE=0
IP_LIST=[]
IP_LIST_DUMMY = [0,1]
MAX_CONNECTION = 3
dummy =0

#----------------------------------------------------------------------------------
#                         BASE CLASS FOR FORKING PORT CONNECTIONS
#----------------------------------------------------------------------------------
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
        while not SYNC_DONE:
            pass
        while local_dummy < MAX_CONNECTION:
            self.csocket.send(bytes(IP_LIST[local_dummy], 'UTF-8'))
            local_dummy = local_dummy + 1
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



LOCALHOST = "192.168.43.126"
PORT = 60069
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
while dummy < MAX_CONNECTION :
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
    IP_LIST.append(clientAddress[0])
    print(IP_LIST)
    dummy = dummy + 1

SYNC_DONE=1



