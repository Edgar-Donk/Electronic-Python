/*
Modified code to use without delay() functions.
*/

int trigPin = 2;
int echoPin = 13;

unsigned long currentTime;
unsigned long loopTime;

unsigned long currentTime2;
unsigned long loopTime2;

long duration;
long distance;

void setup() {
    Serial.begin (9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    }

void loop() {

    currentTime = millis();
    if(currentTime >= (loopTime + 200)){
        ping();
        loopTime = currentTime; // Updates loopTime
    }
}

void ping(){

    digitalWrite(trigPin, HIGH);
    currentTime2 = millis();
    if(currentTime2 >= (loopTime2 + 1000)){
        digitalWrite(trigPin, LOW);
        duration = pulseIn(echoPin, HIGH);
        distance = (duration/2) / 29.1;
        if (distance >= 200 || distance <= 0){
            Serial.println("Out of range");
        }
    else {
        Serial.print(distance);
        Serial.println(" cm");
        }
    loopTime2 = currentTime2; // Updates loopTime2
    }
}