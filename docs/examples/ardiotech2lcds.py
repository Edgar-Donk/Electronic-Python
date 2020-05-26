from tkinter import Tk
import serial
import gaugelib

def Packet():
    # Read the newest output from the Arduino
    dataPacket=ser.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(" ")
    q0=float(splitPacket[0])
    q1=float(splitPacket[1])
    p1.set_value(int(q0))
    p2.set_value(int(q1))
    # root.after(0,Packet)

root = Tk()
p1 = gaugelib.DrawGauge2(
    root,
    max_value=1023,
    min_value=0,
    size=200,
    bg_col='black',
    unit = "Temp. °C",bg_sel = 2)
p1.pack(side='left')

p2 = gaugelib.DrawGauge2(
    root,
    max_value=1023,
    min_value=0,
    size=200,
    bg_col='black',
    unit = "Humid %",bg_sel = 2)
p2.pack(side='right')

ser = serial.Serial('com3', 9600)

while 1:
    Packet()
    root.update() # no root.mainloop()

#root.after(0,Packet)
#root.mainloop()