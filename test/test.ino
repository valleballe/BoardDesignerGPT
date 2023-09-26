#include <Arduino.h>

#define WATER_SENSOR_PIN 2

void setup() {
  pinMode(WATER_SENSOR_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  int waterSensorValue = digitalRead(WATER_SENSOR_PIN);
  Serial.println(waterSensorValue);
  delay(1000);
}