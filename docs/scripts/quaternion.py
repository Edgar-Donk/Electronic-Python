from vpython import *

from serial import Serial

def normalize(v, tolerance=0.001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(tuple(v)), theta

ad=Serial('com3',115200) # this also sends a reset command
sleep(1) # let arduino wake up

scene.title='Quaternion Glider'
scene.width=300
scene.height=300
scene.background=color.cyan
sr = scene.range=25
scene.align="left"

scene.userzoom = False
scene.userspin = False
scene.userpan = False

L = sr*0.75
r = 0.04*L

tube = cylinder(pos=vector(2*r-L/2.0,0,0), radius=r,length=L,
        color=vec(1.0,0.7,0.2))
end = sphere( pos=vector(2*r-L/2.0,0,0), radius=r, color=vec(1.0,0.7,0.2))
end1 = sphere( pos=vector(2*r+L/2.0,0,0), radius=r, color=vec(1.0,0.7,0.2))
cockpit = sphere(pos=vector(4*r-L/2.0,0,0.6*r), radius=r, color=color.gray(0.8))
wing = ellipsoid(pos=vector(0.4*L-L/2.0,0,0),size=vec(0.24*L,2.24*L,r/5),
        color=vec(1,0.32,0.33))
up = box(pos=vector(0.46*L,0,3.6*r),size=vec(4*r,r/5,6*r),color=vec(1,0.62,0))
tail = ellipsoid(pos=vector(0.46*L,0,5.4*r),size=vec(4*r,0.4*L,r/5),
        color=vec(1,0.32,0.33))
plane = compound([tube,end,end1,cockpit,wing,up,tail])

gr = graph(fast=False, ymin=-1, ymax=1.1,width=600,height=300,xmin=0, xmax=10,
        background=color.white,align="right",ytitle='<i>Input</i>',
        xtitle='<i>Time</i>',scroll=True)
f0 = gcurve(color=color.red,label="q0")
f1 = gcurve(color=color.green,label="q1")
f2 = gcurve(color=color.cyan,label="q2")
f3 = gcurve(color=color.orange,label="q3")
f4 = gcurve(color=color.magenta,label="square")
t=0 # time
dt=0.01 # time interval
oldtheta=0

while 'esc' not in keysdown():
    while (ad.inWaiting()>0):
        dataPacket=ad.readline()
        dataPacket=str(dataPacket,'utf-8').strip()
        splitPacket=dataPacket.split(",")
        if len(splitPacket)==4:
            try: # used to eliminate xxx.xx.xx
                #rate(500)
                q0=min(max(float(splitPacket[0]),-1),1)
                q1=min(max(float(splitPacket[1]),-1),1)
                q2=min(max(float(splitPacket[2]),-1),1)
                q3=min(max(float(splitPacket[3]),-1),1)
                sq=q0*q0+q1*q1+q2*q2+q3*q3
                '''
                if t > gr.xmax:
                    d = t-gr.xmax
                    gr.xmin += d
                    gr.xmax += d
                '''
                f0.plot(t,q0)
                f1.plot(t,q1)
                f2.plot(t,q2)
                f3.plot(t,q3)
                f4.plot(t,sq)
                t=t+dt

                if 0.99<q0<1.01:
                    k=vec(1.0,0.0,0.0)
                    theta=0.0
                    plane.axis=k
                else:
                    theta=2*acos(q0)
                    #sinhalftheta=sin(theta/2.0)

                    #k=vec(q1/sinhalftheta,q2/sinhalftheta,q3/sinhalftheta)
                    dtheta=theta-oldtheta
                    k=q_to_axisangle((q0,q1,q2,q3))
                    #print('k',k)
                    #print('vec',(k[0][0],k[0][1],k[0][2]))
                    #plane.axis=vec(k[0][0],k[0][1],k[0][2])
                    plane.rotate(angle=dtheta,axis=vec(k[0][0],k[0][1],k[0][2]))
                    oldtheta=theta

            except ValueError:
                print('data',dataPacket)
        else:
            print('split',splitPacket)

