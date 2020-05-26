# sendASCII.py
# has problem with ASCII 127
# if strip left off have space between lines
    
from time import sleep
import serial

def byte2utf(x):
   # strip before or after decode works
   return(x.decode('utf-8').strip())

ser = serial.Serial('com3', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
   counter +=1
   # str.encode(my_str) convert string to bytes
   # Convert the decimal number to ASCII then send it to the Arduino
   ser.write(str.encode(chr(counter))) 
   # Read the newest output from the Arduino
   print (ser.readline().decode('utf-8')) 
   sleep(.1) # Delay for one tenth of a second
   if counter == 126: # originally 255
      counter = 32