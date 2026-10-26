#include <Wire.h>
#include <Adafruit_AHTX0.h>
#include <DFRobot_ENS160.h>
DFRobot_ENS160_I2C ENS160(&Wire, 0x53);
Adafruit_AHTX0 aht;
#define KY037_PIN A0
void setup() {
  Serial.begin(9600);
  Wire.begin();
  ENS160.setPWRMode(ENS160_STANDARD_MODE);
  aht.begin();
  ENS160.begin();
}
void loop() {
  int noiseValue = analogRead(KY037_PIN);
  sensors_event_t humidity, temp;
  aht.getEvent(&humidity, &temp);
  uint16_t ECO2 = ENS160.getECO2();

  Serial.print(noiseValue);   // Noise first
  Serial.print(",");
  Serial.print(ECO2);         // CO2 second
  Serial.print(",");
  Serial.println(temp.temperature); // Temperature last
  delay(1500);
}
