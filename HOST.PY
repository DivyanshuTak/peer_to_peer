import socket
import string
#====================================================================================================
#             POINTS TO REMEMBER
#  1: python 3 sends a unicode string so bytes string use (b'given string')
#
#
#===================================================================================================
#===========CREATE A SOCKRT OBJECT================================
socket_1 = socket.socket()
#=================================================================
#              DEFINE  THE HOSTNAME ANS THE PORT NUMBER
#=================================================================
ip = "192.168.1.7"  # this ip is when connected to home wifi
#============MENTION OTHER IP ADRESSES HERE=====================
#  IP1::
#  IP2::
#===============================================================
port_num = 60069
indicator = "your message :: "
#=================================================================
#                       ININTIALISE THE HOST
#=================================================================
try:
   socket_1.bind(("192.168.43.126",port_num))
except:
    print("binding error")

message = "this is "
b = "b"
comma = "'"
socket_1.listen(5)
print("host is active")
#========================INITIALISATION COMPLETE===================

#================== STARTING MESSAGES FOR SYNC=======================

client_socket, addr = socket_1.accept()
print("hello mr:", addr)
client_socket.sendall(b'HELLO MOTHERFUCKER')
print(client_socket.recv(1024))
print("type exit to EXIT the chat \n")
print("=================================== \n")

#====================================================================
#                 POLLING OF MESSAGES STARTS HERE
#=====================================================================
while True:
    message_string = input()
    complete_message = indicator + message_string
    #print(complete_message)
    complete_message_string = bytes(message_string , 'utf-8')
    client_socket.sendall(complete_message_string)
    print("\n")
    recieved_message = client_socket.recv(4096)
    print(recieved_message)
    print("\n")
    if(recieved_message == "EXIT"):
        break

#=====================================================================
#                        POLLING OVER
#                        CLOSE THE CHAT
#======================================================================

client_socket.close()




