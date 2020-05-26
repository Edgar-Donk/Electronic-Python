from vpython import *
from serial import Serial

ad=Serial('com3',115200) # this also sends a reset command
sleep(1) # let arduino wake up

gr = graph(fast=False, ymin=-1, ymax=1.1,width=800,height=600,xmin=0, xmax=10,
        background=color.white)
f0 = gcurve(color=color.red,label="q0")
f1 = gcurve(color=color.green,label="q1")
f2 = gcurve(color=color.cyan,label="q2")
f3 = gcurve(color=color.orange,label="q3")
f4 = gcurve(color=color.magenta,label="square")
t=0 # time
dt=0.01 # time interval

while 'esc' not in keysdown():
    while (ad.inWaiting()>0):
        dataPacket=ad.readline()
        dataPacket=str(dataPacket,'utf-8').strip()
        splitPacket=dataPacket.split(",")
        if len(splitPacket)==4:
            try: # used to eliminate xxx.xx.xx
                q0=float(splitPacket[0])
                q1=float(splitPacket[1])
                q2=float(splitPacket[2])
                q3=float(splitPacket[3])
                sq=q0*q0+q1*q1+q2*q2+q3*q3

                if t > gr.xmax:
                    d = t-gr.xmax
                    gr.xmin += d
                    gr.xmax += d

                f0.plot(t,q0)
                f1.plot(t,q1)
                f2.plot(t,q2)
                f3.plot(t,q3)
                f4.plot(t,sq)
                t=t+dt
            except ValueError:
                print('data',dataPacket)
        else:
            print('split',splitPacket)
