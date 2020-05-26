## This program reads data over the serial port from an arduino.
## original had colour detection - need an extra module
## original in v6 - this works in v7

import serial #Import Serial Library
from vpython import * #Import all the vPython library

def raw2utf(x):
    # strip before or after decode works
    return(x.decode('utf-8').strip())

MyScene=canvas(title='My Virtual World', width=800, height= 800,
               centre=vector(12,12,12), background=color.cyan) #Create your scene and give it a title.

#MyScene.width=800  #We can set the dimension of your visual box. 800X800 pixels works well on my screen
#MyScene.height= 800
#MyScene.autoscale=False #We want to set the range of the scene manually for better control. Turn autoscale off
#MyScene.centre = (12,12,12) #Set range of your scene to be 12 inches by 12 inches by 12 inches.

target=box(pos=vector(0,-.5,0), length=.2, width=3, height=3, color=vec(1.0,0.7,0.2)) #Create the object that will represent your target (which is a colored card for our project)
myBoxEnd=box(length=.1, width=10,height=5, pos=vector(-8.5,0,0)) #This object is the little square that is the back of the ultrasonic sensor
myTube2=cylinder(color=color.gray(0.9), pos=vector(-8.5,0,-2.5), radius=1.5,length=2.5 ) #One of the 'tubes' in the front of the ultrasonic sensor
myTube3=cylinder(color=color.gray(0.9), pos=vector(-8.5,0,2.5), radius=1.5,length=2.5 )  #Other tube
myBall=sphere(color=color.red, radius=.3)

arduinoSerialData = serial.Serial('com3', 115200) #Create an object for the Serial port. Adjust 'com11' to whatever port your arduino is sending to.

measuringRod = cylinder( title="My Meter", radius= .5, length=6,
                         color=color.yellow, pos=vector(-3,-2,0))
lengthLabel = label(pos=vector(0,5,0), text='Target Distance is: ', box=False, height=30)
# changed pos=(-3,0,0) to pos=vector(-3,0,0)
# measuringRod.length=37.18


while 1:  #Create a loop that continues to read and display the data
    # rate(20)    #Tell vpython to run this loop 20 times a second
    # inWaiting()==0 # using this locks up measuring
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = raw2utf(arduinoSerialData.readline()) #Read the distance measure as a string
        # changed readline() to readline().strip()
        #print (myData) #Print the measurement to confirm things are working
        distance = float(myData) #convert reading to a floating point number
        measuringRod.length=distance #Change the length of your measuring rod to your last measurement
        target.pos=vector(-6 + distance,0,0)
        myLabel= 'Target Distance is: ' + myData #Create label by appending string myData to string
        lengthLabel.text = myLabel #display updated myLabel on your graphic

