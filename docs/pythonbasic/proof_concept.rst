Proof of Concept
================

.. sidebar:: Viewing the Code

    Just click on the arrow to display or hide the code.

Using just the board without any extra electronic hardware, we can 
communicate directly with the board, and on receiving our message it can
interpret this information and send back processed information. This sleight
of hand relies on the fact that characters can be addressed by their 
character number.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* sendASCII.ino

    .. literalinclude:: ../sketches/sendASCII/sendASCII.ino
        :linenos:

.. note:: Scripts and Sketches

    The python scripts can be found in the scripts directory, the ino 
    sketches in the sketches directory, each in its own subdirectory. You
    may find it useful to put the python scripts in the subdirectory of the
    associated sketch.

As you can see we are using the standard format for the Arduino sketch. No
libraries are required, so straight in with the setup where just the serial
port needs to be installed. After that the loop function, where we hold the
board back until after the serial port becomes available. Plug the Arduino 
into the serial port and compile the program, which stays on the Arduino
until the next program is compiled, even when the power source is 
disconnected. 

Now sort out the Python part, you can leave the Arduino on or off the serial 
port.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* sendASCII.py

    .. literalinclude:: ../scripts/sendASCII.py
        :linenos: 

After importing serial and time we open the serial port - adjust to suit your 
operating system - there is no need to start the Arduino, just plug in the
serial port to the Aeduino, it automatically detects the receiver on the 
serial port. Once the Arduino starts to transmit the computer in turn starts 
to transmit information which is then returned before printing the received 
information. You will notice that the main computer is encoding and decoding 
the data, leaving the Arduino simply to read and retransmit the same data. 