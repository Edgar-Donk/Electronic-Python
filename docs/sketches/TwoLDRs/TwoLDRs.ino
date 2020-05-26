// analogue-plot
// 
// Read analogue values from A0 and A1 and print them to serial port.
/*
    Component      Connect       to and to
    LDR right leg  arduino 5V
    LDR left leg   arduino A0
    LDR left leg   4.7kΩ resistor arduino GnD
    LED long leg   arduino pin 10
    LED short leg  220Ω resistor  arduino GnD

    LDR right leg  arduino 5V
    LDR left leg   arduino A1
    LDR left leg   4.7kΩ resistor arduino GnD
    LED long leg   arduino pin 11
    LED short leg  220Ω resistor  arduino GnD
*/

int Vdivid0 = A0;                  // voltage divider analog pin
int LEDpin0 = 10;                  // LED on PWM pin
int Vdivid1 = A1;                  // voltage divider analog pin
int LEDpin1 = 11;                  // LED on PWM pin
int thresh = 500;                 // threshold light intensity
int reading0, bright0, reading1, bright1;
void setup()
{
    Serial.begin(9600);
    pinMode(LEDpin0, OUTPUT);        // LED pin as output
    pinMode(LEDpin1, OUTPUT);        // LED pin as output
    }
        
void loop()
{
    reading0 = analogRead(Vdivid0);   // voltage divider reading
    bright0 = 0;                     // set LED brightness to zero
                                    // map reading to LED brightness
    if(reading0<thresh) bright0 = map(reading0, 0, thresh, 255, 0);
    analogWrite(LEDpin0, bright0);    // change LED brightness
  
    reading1 = analogRead(Vdivid1);   // voltage divider reading
    bright1 = 0;                     // set LED brightness to zero
                                  // map reading to LED brightness
    if(reading1<thresh) bright1 = map(reading1, 0, thresh, 255, 0);
    analogWrite(LEDpin1, bright1);    // change LED brightness
  
    // print to serial
    Serial.print(reading0);
    Serial.print(" ");
    Serial.print(reading1);
    Serial.print("\n");

    delay(1000);                    // delay 1000ms
    }
