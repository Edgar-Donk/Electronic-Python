Two Light Detecting Resistors
=============================

.. sidebar:: Voltage Divider

    Using a resistance one can bias the output voltage to give the required
    voltage output. When the LCD has 500 Ω Vout is 4.5 V but when 50 kΩ Vout 
    is 0.43 V:: 
    
        Vout = Vin ( Rresistor / (Rlcd + Rresistor))

This setup is slightly more interesting, we use two light detecting 
resistors (LDR) that have a variable resistance inversely dependant on the
light. Near dark they are about 50 kΩ and 500 Ω in bright light. The Arduino
can measure voltage so it is combined with a resistor to enable the Arduino
to function. The LDR is connected to 5V and the other leg goes to a junction
between the analogue pin and a 4.7 kΩ resistor that is connected to ground.
This setup acts as a voltage divider. As a bonus we can trigger a LED when a 
threshold is reached. These values are dependant on the LDR characteristic
and the light level.

.. container:: toggle

    .. container:: header

        *Show/Hide Code* TwoLDRs.ino

    .. literalinclude:: ../sketches/TwoLDRs/TwoLDRs.ino
        :linenos:

.. note:: The leds must always be protected from overcurrent, on a 5V supply
    
    a 220Ω resistor is suitable.

.. sidebar:: Did your LED swich on and off?

    If no, then replace one of the high resistors with a 10 kΩ potentiometer.
    Vary the resistance until the desired switchpoint, now replace the
    other high resistor and potentiometer with the nearest high resistor
    as measured on the potentiometer.

Map is a useful function to ensure that the Arduino works in the correct
range, the first value (in our case reading0 and reading1) is the variable
under consideration. The next two values are the first range, fromLow and 
fromHigh, the last two values are the second range, toLow and toHigh. In our
case we are swopping the high and low values in the second range since
resistance increases with brightness. The output of map is an integer.

.. comments
.. comments
.. comments
.. comments
.. comments

.. topic:: Mapping with more precision

    If higher precision is required then avoid map() and use your own code::
    
        long map(long x, long in_min, long in_max, long out_min, long out_max) {
            return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
            }


In the first example we had only one value to send and this was simply a
println. In the current example there are two values in every data packet.
This means we need to send the first piece of data followed by a separator,
the second piece of data followed by a return (we could have sent a println 
with the second piece).

As it stands we can check the output on the serial monitor and the serial 
plotter. When satisfied it creates the right output, we can tie into a python
application. We could simply print the results within a console or Idle.

There are more interesting possibilities. 