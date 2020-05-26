===========
Calibration  
===========

IMU_Zero
--------

Before running any of the measurement programs, with the MPU6050 showing 
acceleration in any direction first run IMU_Zero.ino, this is a calibration 
program and requires the unit to be placed on a level surface for 10 to 15
minutes. As long as the gravity is 1g then it should calibrate. The offsets
are printed, these should be saved as they will be used in later scripts. If
you happen to have more than one module then each will need its own 
calibration and identification. 

The address is normally 0x68 and this is explained in the sketch. 

.. container:: toggle

    .. container:: header

        *Show/Hide Code* IMU_Zero.txt

    .. literalinclude:: ../examples/IMU_Zero.txt
        :emphasize-lines: 28-29, 60

So the offsets I should use is for example 1334 for XAccel, the bracketed 
value following [1333,1334] is a confidence limit.

Raw MPU6050 Data
----------------

Now look at MPU6050_raw.ino, this will give us 

* XAccel

* YAccel

* ZAccel

* XGyro

* YGyro

* ZGyro

.. sidebar:: Reading the Output

    The output fills the page pretty quickly, the Arduino waits for the
    serial monitor to be connected, so start the monitor then pull out the
    serial connection to stop the serial monitor. Now copy the output.
    
    If the output cannot be read, check the baud rate, otherwise unplug and
    restart - there normally is no need to recompile.

The accelerometer is set to ±2g, the raw 16 bit register gives 65536 (2**16)
therefore to obtain the readings in g divide 65536 by 4 to obtain 16384. The 
gyroscope is set to ±250°/sec, so to obtain the actual change in degrees per 
second divide 65536 by 500 gives 131.07, round this figure 131 and divide
the raw values to give the gyroscope readings.

Each will have its own offset, an example has been shown in the original
script, run it as it is and check the output, before changing. He has a 
choice of human readable output, or binary, as we are working with the 
serial monitor choose human readable. Don't get caught out by the change in 
baud rate, he's using 38400. You should see something like the following
output if the module is left standing::

    Testing device connections...
    MPU6050 connection successful
    a/g:	1552	48	15776	1207	22	-591
    a/g:	1568	4	15960	1200	2	-599
    a/g:	1624	-8	15656	1179	13	-607
    a/g:	1540	-48	15712	1193	30	-567
    a/g:	1516	20	15816	1181	17	-583
    a/g:	1444	-28	15684	1185	24	-597
    a/g:	1604	24	15784	1168	27	-579
    a/g:	1524	-20	15832	1188	5	-578

Considering that my unit needed the following offsets ::

    1334 -2407 1659 -77 69 62

Not too bad, uncomment updating the offsets and put in your values, once 
again leave the module standing and check the results::

    Initializing I2C devices...
    Testing device connections...
    MPU6050 connection successful
    Updating internal sensor offsets...
           1520  -2407       1582    0   0      0   
           1334  -2407       1659  -77  69     62	
    a/g:     56     48      16384    4 -15    117
    a/g:    -16      0      16516   16   5     20
    a/g:    -76     68      16364   -2 -51     12
    a/g:     68     64      16472   -4 -40    -12
    a/g:    -28     52      16348  -22 -29     -7
    a/g:    -60    -44      16388   -6  -3     10
    a/g:    -76     20      16356   -9   6    -20
    a/g:    -96    -20      16504   -6   8     37

You should see something similar with your results, remember that the values 
should all be around 0 apart from the ZAccel which should be about 16384. 

Having sorted out the offsets, the raw data is no longer so interesting.
