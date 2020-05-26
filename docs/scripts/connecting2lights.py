import serial

# Establish the connection on a specific port
ser = serial.Serial('com3', 9600)
while True:
    # Read the newest output from the Arduino
    dataPacket=ser.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(" ")
    q0=float(splitPacket[0])
    q1=float(splitPacket[1])
    print (q0,q1)