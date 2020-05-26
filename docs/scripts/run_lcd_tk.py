from tkinter import Tk,Frame

import serial
from lcd_tk import LCD

oldq0=511
oldq1=511

def Packet(oldq0,oldq1):
    # Read the newest output from the Arduino
    dataPacket=ser.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(" ")
    q0=int(splitPacket[0])
    q1=int(splitPacket[1])
    l1.lcd_pointer(q0,oldq0)
    l2.lcd_pointer(q1,oldq1)
    return q0,q1

root = Tk()
fr=Frame(root)
fr.grid(row=0,column=0,sticky='nsew')

l1=LCD(fr,select=4,enlargement=2,colour='red',unit='Luminosity')
l1.grid(row=0,column=0,sticky='nsew')
l2=LCD(fr,select=4,enlargement=2,colour='green',unit='Luminosity')
l2.grid(row=0,column=1,sticky='nsew')


ser = serial.Serial('com3', 9600)

while 1:

    q0,q1=Packet(oldq0,oldq1)

    oldq0=q0
    oldq1=q1
    root.update() # no root.mainloop()