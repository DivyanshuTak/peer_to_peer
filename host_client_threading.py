import socket
import _thread
import threading
#----------------------------------------------------------------------
#                           HOST FUNCTION
#----------------------------------------------------------------------
def local_host():


    socket_1 = socket.socket()
    # =================================================================
    #              DEFINE  THE HOSTNAME ANS THE PORT NUMBER
    # =================================================================
    local_host1 = socket.gethostname()
    ip = socket.gethostbyname(local_host1)
    print(ip)
    print(local_host1)
    port_num = 60069
    try:
        socket_1.bind((local_host1, port_num))
    except:
        print("binding error")

    socket_1.listen(5)
    print("host is active")

    # ==================POLLING STARTS FOR CLEINT=======================
    while True:
        client_socket, addr = socket_1.accept()
        print("hello mr:", addr)
        client_socket.send(b'HELLO MOTHERFUCKER')
        data = client_socket.recv(1024)
        print(data)
        client_socket.close()

#----------------------------------------------------------------------
#                           FUNCTION END HERE
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#                           CLIENT  FUNCTION
#----------------------------------------------------------------------

def local_client():
    client_socket = socket.socket()
    # ===================================================================
    #                  CLIENT INITIALISATION
    # ===================================================================
    client_ip = socket.gethostname()
    port = 60069
    print(client_ip)
    client_socket.connect((client_ip, port))
    # ======================================================================
    #                   ININTIALISATION COMPLETE
    # ======================================================================
    #                SEND ANS RECIEVE DATA HERE
    # ======================================================================
    print(client_socket.recv(1024))
    client_socket.send(b'hello')
    # ======================CLOSE THE CONNECTION============================
    client_socket.close()
#----------------------------------------------------------------------
#                          FUNCTION ENDS HERE
#----------------------------------------------------------------------

try:
    _thread.start_new_thread(local_host,())
   # _thread.start_new_thread(local_client,())
except:
    print("not able to start the thread")

print(threading.active_count())


while 1:
    pass

