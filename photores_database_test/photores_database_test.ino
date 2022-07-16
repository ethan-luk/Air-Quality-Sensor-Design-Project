#include <ArduinoJson.h>

int analogPin = A0;
int val = 0;
int num = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  num = num + 1;
  StaticJsonDocument<100> data;
  data["hi"] = val;
  data["num"] = num;
  serializeJson(data, Serial);
  Serial.println();
//Serial.setTimeout(3000);
  delay(5000);
}
