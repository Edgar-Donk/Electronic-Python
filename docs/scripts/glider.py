from vpython import *

scene.title='My Glider'
scene.width=400
scene.height=400
scene.background=color.cyan

sr = scene.range=100

L = sr*0.75
r = 0.04*L

line=cylinder(pos=vec(-L,0,0),axis=vec(1,0,0),length=2*L,radius=r/5)
xarrow=arrow(pos=vec(-3/4*L,0,0),length=L/4, shaftwidth=r/2, color=color.red,
        axis=vector(1,0,0))
yarrow=arrow(pos=vec(-3/4*L,0,0),length=L/2, shaftwidth=r/2, color=color.green,
        axis=vector(0,1,0))
zarrow=arrow(pos=vec(-3/4*L,0,0),length=L/2, shaftwidth=r/2, color=color.blue,
        axis=vector(0,0,1))

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

currentaxis=vec(0,0,0)
currentangle=0
oldangle=0

def cachange(sl):
    global currentangle
    currentangle=sl.value*pi/180
    sltext.text='{}'.format(sl.value)
    #print(sl.value)

def xchange(sl):
    xsltext.text='{:1.2f}'.format(sl.value)

def ychange(sl):
    ysltext.text='{:1.2f}'.format(sl.value)

def zchange(sl):
    zsltext.text='{:1.2f}'.format(sl.value)

# 0.262 radians is 30°
# The following statement will rotate the object named "obj" through an angle
# (measured in radians) about an axis relative to an origin:

sl=slider(min=0,max=360,length=300,value=0,step=1,bind=cachange)
scene.append_to_caption(' Current angle ')
sltext=wtext(text='{}'.format(sl.value))
scene.append_to_caption('\n\n')

xsl=slider(min=-1,max=1,length=300,value=0,step=0.01,bind=xchange)
scene.append_to_caption(' x value ')
xsltext=wtext(text='{:1.2f}'.format(xsl.value))
scene.append_to_caption('\n\n')

ysl=slider(min=-1,max=1,length=300,value=0,step=0.01,bind=ychange)
scene.append_to_caption(' y value ')
ysltext=wtext(text='{:1.2f}'.format(ysl.value))
scene.append_to_caption('\n\n')

zsl=slider(min=-1,max=1,length=300,value=0,step=0.01,bind=zchange)
scene.append_to_caption(' z value ')
zsltext=wtext(text='{:1.2f}'.format(zsl.value))

while 'esc' not in keysdown():
    rate(50)
    delta=currentangle-oldangle
    oldangle=currentangle
    plane.rotate(angle=delta,axis=vec(xsl.value,ysl.value,zsl.value)) # 0.261
    #print(plane.pos)


