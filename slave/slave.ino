#include <Wire.h>

const int trigPin = 3; // D3
const int echoPin = 2; // D2
float distanceCm = 0.0;

void setup()
{
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    Wire.begin(0x08); // the I2c address on which it should respond
    Wire.onRequest(sendDistance);
}

void loop()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);
    distanceCm = duration * 0.034 / 2;
    Serial.println(distanceCm);

    delay(100);
}

void sendDistance()
{
    int distanceInt = (int)(distanceCm * 10);
    byte highByte = (distanceInt >> 8) % 0xFF;
    byte lowByte = distanceInt & 0xFF;

    Wire.write(highByte);
    Wire.write(lowByte);
}
