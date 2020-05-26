========================
Inertia Measurement Unit
========================

Introduction IMU
----------------

This is a relatively small unit that has quite amazing capabilities. Be 
careful about what your unit is called, in the Elgoo kit they have a unit
called ``GY-521``, which can sense acceleration in all 3 axes and has an 
inbuilt gyro and arithmetic processing unit, or Digital Motion Processor DMP. 
Some more expensive units also have a magnetometer, which stabilises the 
output preventing a drift in the output, althogh just using a 6 axis module
with the DMP should give accurate enough results.

To make this work use the library supplied, thanks to Jeff Rowberg who spent
a great deal of time sorting out what these units get up to, he uses the
nomenclature ``MPU6050`` the current version version is at
`MPU6050 <https://github.com/jrowberg/i2cdevlib>`_. Assume that both MPU6050
and GY-521 are similar, just that GY-521 is a built-up module.

The original library completed in 2013 to 2014, has several files found 
under i2cdevlib/MSP430/MPU6050

* MPU6050.cpp 

* helper_3dmath.h 

* MPU6050.h 

* MPU6050_6Axis_MotionApps20.h 

* MPU6050_9Axis_MotionApps41.h 

plus a directory of Examples

* MPU6050_raw.ino 

* MPU6050_DMP6.ino 

the last has a Processing subdirectory

* MPUTeapot.pde 

which produces a visual output in Processing.

The revised version is now the current version found under i2cdevlib/Arduino/MPU6050

* MPU6050.cpp 

* helper_3dmath.h 

* library.json 

* MPU6050.h 

* MPU6050_6Axis_MotionApps20.h 

* MPU6050_9Axis_MotionApps41.h 

plus a directory of Examples

* IMU_Zero 

* MPU6050_raw.ino 

* MPU6050_DMP6.ino 

* MPU6050_DMP6_ESPWiFi.ino 

* MPU6050_DMP6_using_DMP_V6.12.ino 

the MPU6050_DMP6 has a Processing subdirectory with MPUTeapot.pde

If you want to run both libraries make sure that each library has different
names and that the references are updated as necessary.

.. sidebar:: Does your IMU have a Magnetometer?

    If your IMU unit includes a magnetometer, such as the Adafruit BNO055 
    then the sketches from Paul McWhorter can be used.

As can be seen there are quite a number of possible testing possibilities, 
so I shall dwell mainly on the newer library from Jeff Rowberg, with a spice
from Paul McWhorter to help with vpython. 

