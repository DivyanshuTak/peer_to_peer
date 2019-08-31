import serial
import os
import sys
import numpy as np
import subprocess
import time
import esp2 as esp

MAX_VOLTAGE=10
MAX_VALUE = 32767
volt_string = [0,0,0,0]
#freq_string = [0,0,0]
output = 0x0000
ret_val=0
adjust = 0.02
lsb = 15
lsb2 = hex(lsb)
temp = 0x0000
data = 0x0000
freq_value=0
theta = 0
start_freq = 1
freq_step = 0
freq_limit = 8



filepath = "E:\dnNIDLL"
file = "LCVRRESPONSE.exe"
des_path = "D:\Freq"

def voltage_to_hex(voltage):
    a=0
    decimal = int((float(voltage)/MAX_VOLTAGE)*MAX_VALUE + 1)
    return hex(decimal)

def voltage_to_string(input):
    if len(input) == 6:
        sliced = input[2:]
    elif len(input) == 5:
        sliced = str('0') + input[2:]
    elif len(input) == 4:
        sliced = str('00') + input[2:]
    elif len(input) == 3:
        sliced = str('000') + input[2:]
    print(sliced)
    for a in range(len(volt_string)):
        temp = sliced[a]#input[a+2]
        if temp == 'a':
            volt_string[a] = 'A'
        elif temp == 'b':
            volt_string[a] = 'B'
        elif temp == 'c':
            volt_string[a] = 'C'
        elif temp == 'd':
            volt_string[a] = 'D'
        elif temp == 'e':
            volt_string[a] = 'E'
        elif temp == 'f':
            volt_string[a] = 'F'
        elif temp == '0':
            volt_string[a] = 0
        elif temp == '1':
            volt_string[a] = 1
        elif temp == '2':
            volt_string[a] = 2
        elif temp == '3':
            volt_string[a] = 3
        elif temp == '4':
            volt_string[a] = 4
        elif temp == '5':
            volt_string[a] = 5
        elif temp == '6':
            volt_string[a] = 6
        elif temp == '7':
            volt_string[a] = 7
        elif temp == '8':
            volt_string[a] = 8
        elif temp == '9':
            volt_string[a] = 9

def freq_to_string(freq):
    str1 = str(freq)
    freq_string = []
    for c in range(len(str1)):
        freq_string.append(str1[len(str1) - c-1])
    if len(freq_string)!= 4:
        diff = 4-len(freq_string)
        for t in range(diff):
            freq_string.append('0')
    return freq_string



if __name__ == "__main__":

    try:
        ComPort = serial.Serial('COM9')  # open COM9
    except:
        print("failed to open the port")
    ComPort.baudrate = 9600  # set Baud rate to 9600
    ComPort.bytesize = 8  # Number of data bits = 8
    ComPort.parity = 'N'  # No parity
    ComPort.stopbits = 1  # Number of Stop bits = 1

    esp.initialise(1)

    # ----------------------------------------------------------------------------------------------
    # =============================================================================================
    #                           LOOPING STARTS FOR DATA AQUESITION
    # ==============================================================================================
    # ----------------------------------------------------------------------------------------------
    delay = input("enter to start")
    while freq_value <= freq_limit:
        #epoch = input("start another epoch??")
        epoch = "y"
        if epoch == "y":

            voltage = 0.0001
            volt_limit = 2   #2.2
            step = 0.0125    #0.0125
            data2 = str("f").encode()
            No = ComPort.write(data2)
            rec = ComPort.read()
            if rec.decode() != "f":
                print("waiting here")
            else :
                print("continue")
            if rec.decode() == "f":  ## SEND THE SPECIFIED FREQUENCY
                freq_value = start_freq+freq_step#input("enter frequency value")
                print("==================================================================================================")
                print(freq_value)
                print("===================================================================================================")
                ret_val = freq_to_string(freq_value)
                for a in range(len(ret_val)):
                    print(ret_val[a])
                    data2 = str(ret_val[a]).encode()
                    No = ComPort.write(data2)

            # yes = input("loop for voltage")
            # if yes == "y":
            #    data2 = str("v").encode()
            #    No = ComPort.write(data2)
            #    rec = ComPort.read()

            start_time = time.time()
            while (time.time() - start_time < 2):
                loop = 1
            start = "y"#input("start aquiring data??")

            theta = 90
            print(float(theta))
            esp.move(1, float(theta))
            start_time = time.time()
            while (time.time() - start_time < 15):
                loop = 1
            if start == "y":
                while voltage < volt_limit:
                    voltage_to_string(voltage_to_hex(voltage + adjust))
                    os.startfile(os.path.join(filepath,
                                              file))  # p = subprocess.Popen(os.path.join(filepath, file))  # os.startfile(os.path.join(filepath, file))
                    start_time = time.time()
                    print(voltage)
                    while (time.time() - start_time < 1.5):
                        loop = 1
                    data2 = str("v").encode()
                    No = ComPort.write(data2)
                    rec = ComPort.read()
                    start_time = time.time()
                    while (time.time() - start_time < 0.2):
                        loop = 1
                    for a in range(len(volt_string)):
                        # print(volt_string[a])
                        data2 = str(volt_string[a]).encode()
                        No = ComPort.write(data2)
                    # ========================================WAIT FOR THE PROCESS TO COMPLETE==================
                    start_time = time.time()
                    while (time.time() - start_time < 2.9):      #3
                        loop = 1
                    # time.sleep(4)  # Delays for 4 seconds.
                    # poll = p.poll()
                    # while poll == None:
                    #    poll = p.poll()
                    # =========================================PROCESS IS COMPLETED==============================
                    f = open("DataNIAD_temp.txt")
                    name = "DataNIAD_THETA=" + str(theta) + "freq=" + str(freq_value) + "KHZ_" + str(
                        voltage) + "volts" + ".txt"
                    f1 = open(os.path.join(des_path, name), "w")
                    for x in f.readlines():
                        f1.write(x)
                    f.close()
                    f1.close()
                    voltage += step

            theta = 0
            esp.move(1, float(theta))
            voltage = 0.0001
            # ============================================delay until the esp reaches the required value============================
            start_time = time.time()
            while (time.time() - start_time < 10):
                loop = 1
            # ======================================================================================================================
            if start == "y":
                while voltage < volt_limit:
                    voltage_to_string(voltage_to_hex(voltage + adjust))
                    os.startfile(os.path.join(filepath,
                                              file))  # p = subprocess.Popen(os.path.join(filepath, file))  # os.startfile(os.path.join(filepath, file))
                    start_time = time.time()
                    print(voltage)
                    while (time.time() - start_time < 1.5):
                        loop = 1
                    data2 = str("v").encode()
                    No = ComPort.write(data2)
                    rec = ComPort.read()
                    start_time = time.time()
                    while (time.time() - start_time < 0.2):
                        loop = 1
                    for a in range(len(volt_string)):
                        # print(volt_string[a])
                        data2 = str(volt_string[a]).encode()
                        No = ComPort.write(data2)
                    # ========================================WAIT FOR THE PROCESS TO COMPLETE==================
                    start_time = time.time()
                    while (time.time() - start_time < 3):
                        loop = 1
                    # time.sleep(4)  # Delays for 4 seconds.
                    # poll = p.poll()
                    # while poll == None:
                    #    poll = p.poll()
                    # =========================================PROCESS IS COMPLETED==============================
                    f = open("DataNIAD_temp.txt")
                    name = "DataNIAD_THETA=" + str(theta) + "freq=" + str(freq_value) + "KHZ_" + str(
                        voltage) + "volts" + ".txt"
                    f1 = open(os.path.join(des_path, name), "w")
                    for x in f.readlines():
                        f1.write(x)
                    f.close()
                    f1.close()
                    voltage += step
        freq_step += 1

        #data2 = str("v").encode()
        #No = ComPort.write(data2)
        #rec = ComPort.read()
        #voltage_to_string(voltage_to_hex(0.01))
        #start_time = time.time()
        #while (time.time() - start_time < 0.2):
        #    loop = 1
        #for a in range(len(volt_string)):
        #    # print(volt_string[a])
        #    data2 = str(volt_string[a]).encode()
        #    No = ComPort.write(data2)

'''

while True:
    dec = input("enter f for freq and v for voltage")
    data2 = str(dec).encode()
    No = ComPort.write(data2)
    rec = ComPort.read()
    if rec.decode() == "f":                                                                                             ## SEND THE SPECIFIED FREQUENCY
        value = input("enter value")
        ret_val = freq_to_string(value)
        for a in range(len(ret_val)):
            print(ret_val[a])
            data2 = str(ret_val[a]).encode()
            No = ComPort.write(data2)

    elif rec.decode() == "v":                                                                                           ## SEND THE VOLTAGE STORED IN VOLT_STRING VARIABLE
        value = input("enter the voltage value")
        voltage_to_string(voltage_to_hex(value))
        for a in range(len(volt_string)):
            print(volt_string[a])
            data2 = str(volt_string[a]).encode()
            No = ComPort.write(data2)
            #rec = ComPort.read()
            #print(rec)

'''


'''

c = input("enter the voltage ")
#output = voltage_to_hex(c)
#print(output)
#print(hex(output))
#d = hex(output)

voltage_to_string(voltage_to_hex(c))
print(volt_string)

#char = str(0x000F)
#while True:
#    print(char)

try:
    ComPort = serial.Serial('COM9')  # open COM9
except:
    print("failed to open the port")
ComPort.baudrate = 9600 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1

#while True:
#    volt = float(input("enter the voltage::"))
#    data = voltage_to_hex(volt)




a = input("do you want to contiue?")
if a == "yes":
    number = input("enter the character")
    number = 23
   # print(number)
   # print(int(number))
    data2 = str(number).encode()
No = ComPort.write(data2)
print(No)



rec = ComPort.read()
print(rec)




a = input("do you want to contiue?")




















#import serial           # import the module
try:
    ComPort = serial.Serial('COM9')  # open COM9
except:
    print("failed to open the port")
ComPort.baudrate = 9600 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1
byte=0x45
number = 'A'
data2 = str(number).encode()
data =  bytearray(B'A')
print("data sent")

a=0

#while True:
#    a = input("do you want to contiue?")
#    if a == "y":
#        number = input("enter the character")
        # print(number)
        # print(int(number))
#        data2 = bytes(number, 'ascii')  # np.uint8(number)#str(number).encode()
#    No = ComPort.write(data2)
#    print(No)


#rec = ComPort.read()
#print(rec)


a = input("do you want to contiue?")
if a == "yes":
    number = input("enter the character")
    number = 0x000A
   # print(number)
   # print(int(number))
    data2 = str(number).encode()
No = ComPort.write(data2)
print(No)



rec = ComPort.read()
print(rec)



while True:
    a = input("do you want to contiue?")
    if a == "yes":
        number = input("enter the character")
        print(number)
        print(int(number))
        data2 = str(number).encode()
    No = ComPort.write(data2)
    print(No)









#while True:
#    rec = ComPort.read()
#    print(rec)


#ser = serial.Serial()
#ser.port = "/dev/ttyUSB0"
#ser.baudrate = 9600
#ser.bytesize = serial.EIGHTBITS #number of bits per bytes
#ser.parity = serial.PARITY_NONE #set parity check: no parity
#ser.stopbits = serial.STOPBITS_TWO #number of stop bits

    #ser.timeout = None          #block read
#ser.timeout = 5               #non-block read
    #ser.timeout = 2              #timeout block read
#ser.xonxoff = False     #disable software flow control
#ser.rtscts = False     #disable hardware (RTS/CTS) flow control
#ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

#try:
#    ser.open()
#except :#Exception, e:
#    print("error open serial port: " )
#    exit()

#if ser.isOpen():
#    print("serial port is open")
'''