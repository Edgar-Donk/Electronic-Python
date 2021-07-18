Common Arduino Commands
=======================

Table Common Arduino Commands
-----------------------------

The commands shown below are those special ones used by the Arduino mainly
for communication to the electronic components or modules. The serial 
commands are for communication after the sketch is running. As already 
stated the sketches are as brief as possible all the complicated programming
being delegated to the libraries, which enable communication with the
electronic hardware.

.. csv-table:: Arduino_commands.csv
   :file: ../csv_data/Arduino_commands.csv
   :header-rows: 1
   :delim: $
   :widths: 20, 45, 75

.. note:: If you prefer you can view this or the other tables in python
    using treeview, open file ``tree.py`` in the scripts directory, and 
    change the csv file name and csvDelimiter, lines 77-78.

It is also possible that no continuous serial communication is needed, 
especially when using lcd displays and the like. These configurations are 
useful when prototyping systems, that will run independantly of the main 
computer.

Some of the above commands are limited by the constraints of the Arduino 
chip it can only read between 0 and 1023 bytes, and can only write between
0 and 255 bytes. Floating point arithmetic on the Arduino takes a long 
time to obtain poor results, delegate this to the host computer. Where 
possible do as much as possible using bytes or unsigned integers rather than 
normal integers. 