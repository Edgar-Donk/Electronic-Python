Pin Configurations
==================

Each Arduino board have different pins for various functions, these differ 
between boards and the user must take care to correctly connect according to
the board type. These are labelled, generally most sketches refer to the Uno
board, so be careful when using another board.

.. csv-table:: Arduino_pins.csv
   :file: ../csv_data/Arduino_pins.csv
   :header-rows: 1
   :delim: ;
   :widths: 15, 25, 35, 30

Most of the commands allow the program to operate synchronously, delay()
prevents the Arduino from doing anything else. Interrupts allow asynchronous
operation, so that fast events can be detected during a slower process. Only
a few reserved pins can be used for this process.

Table Arduino Interrupt Pins
----------------------------

.. csv-table:: Arduino_interrupt_numbers.csv
   :file: ../csv_data/Arduino_interrupt_numbers.csv
   :header-rows: 1
   :delim: ,
   :widths: 15, 3, 3,3,3,3,3,45