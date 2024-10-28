Basic needs Python
==================

.. sidebar:: Serial Communication

    Synchronise baud rates and serial port at the ino sketch and python 
    script. Modern serial communication automatically detects settings, such 
    as parity, stopbits and bytesize. 

All that is really necessary is to install pySerial, ``pip install pyserial``,
then set up serial in the python script. There is no problem with Python 3 
or 64 bit computing. Pyserial communicates directly using binary 
transmission - so communication is simple for the user. 

Just for information the Arduino uses 8 data bits, no parity and one stop bit.

There are other packages such as pyfirmata, Firmata and Arduino-Python3 that
can be used on the Arduino. Using these one can load a python script and run 
it on the Arduino, unfortunately most of the libraries have not been 
translated into Python. So other than simple sketches there is no easy way 
to directly program the Arduino. Ontop of that expect to use up a lot of 
available Arduino memory. So other than for interest it is probably best 
left alone. 

For the moment it is best to accept the minor annoyance of coding the 
Arduino in C/C++, let it obtain and transmit the information, then 
transform it to something interesting in Python.