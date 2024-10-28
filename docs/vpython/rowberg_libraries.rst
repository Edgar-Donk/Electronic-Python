
===========================
MPU-6050 and Wire Libraries
===========================

Wire Library
------------

As there are a number of outputs from the module it makes sense to wire using
the I2C (Inter Integrated Circuit) protocol. This means we will be importing
the ``Wire`` library, this protocol uses a floating value allowing a 2-way flow
of information. Only specific pins can be used, Uno uses pins A4 and A5,
whereas Mega uses pins 20 and 21 marked SDA and SCL. This means there are
often only 4 connections, the other two being power (3.3V) and ground (GND).

You should see 4 more connections, these are used for specific sketches.

.. warning:: Supply Voltage - be careful there was a dispute in the internet
    as to the correct supply voltage. This should have been handled by the
    supplier, but to be safe try it out with 3.3V, if it works continue. A 
    bare MPU works on 3.3V, the GY-521 module should have a voltage 
    regulator allowing 5V operation.

In most of the sketches a wakeup call is required to activate the IMU unit, 
also you should find a method of addressing the unit, since there could be
several different I2C modules working together::

    const int MPU_ADDR=0x68; // I2C address of the MPU-6050. 
    // If AD0 pin is set to HIGH, the I2C address will be 0x69.

Using MPU6050 Library
---------------------

As I have both the libraries from Jeff Rowberg in my libraries directory,
the one used is referred to as ``NewMPU6050`` in my scripts. If you needed to
import this from the website be sure to have a different name from your
original.

When using the NewMPU6050 library the library I2Cdev has also been called,
which has also been imported new and renamed NewI2Cdev. Since Jeff appears
to know what he is doing, I have not changed anything else apart from 
references to the new files in the file name and references within the cpp 
and h files.
