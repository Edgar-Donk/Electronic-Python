from time import time
import serial
from vpython import *

gd=graph(xmin=0,xmax=10,width=600,height=400,
title='Light Detecting Resistor',xtitle='Time',
ytitle='Arduino Output',scroll=True,fast=False)

output0=gcurve(color=color.red, label='red LED')
output1=gcurve(color=color.green, label='green LED')

# Establish the connection on a specific port
ser = serial.Serial('com3', 9600)
start = round(time())
while True:
    # Read the newest output from the Arduino
    dataPacket=ser.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(" ")
    q0=float(splitPacket[0])
    q1=float(splitPacket[1])

    now=round(time())
    output0.plot(pos=(now-start,q0))
    output1.plot(pos=(now-start,q1))