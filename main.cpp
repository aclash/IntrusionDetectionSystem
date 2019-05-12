#include <Arduino.h>
#define PIR 23
void setup() {
	Serial.begin(9600);
	pinMode(PIR,INPUT); 
}

void loop() {
	bool motion = digitalRead(PIR); // Read the PIR
	if (motion)
		Serial.println(1);
	else
		Serial.println(0);
	delay(3000);
}