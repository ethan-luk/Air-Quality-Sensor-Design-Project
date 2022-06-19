#include <SoftwareSerial.h> // SoftwareSerial reads serial data --> returns GPS data in NMEA format (standard for GPS industry)
#include <TinyGPS++.h>
#include <TinyGPSPlus.h>  // TinyGPSPlus parses the NMEA format and turns it into readable data
#include <ArduinoJson.h>  // ArduinoJson v6 - send serial data in JSON format from Arduino

/*  Serial connection to GPS module using:
 *  RX pin connected to Arduino pin 3 - Pin to receive data
 *  TX pin connected to Arduino pin 4 - Pin to transmit data
 */

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 9600; //unsigned int (32 bit) where _t says the size is standard across platforms
const int capacity = JSON_OBJECT_SIZE(4);

// instantiating objects
TinyGPSPlus gps; 
SoftwareSerial ss(RXPin,TXPin);

void setup() {
  Serial.begin(9600);
  ss.begin(GPSBaud);
}

void loop() {
  
  // .available() returns number of bytes ready to read
  while (ss.available() > 0) {  
    gps.encode(ss.read());
    
    if (gps.location.isUpdated()){
      latitude = gps.location.lat();  // type double
      longitude = gps.location.lng(); // type double

      dat = gps.date.value(); // type unsigned 32 bit int
      tim = gps.time.value(); // type unsigned 32 bit int
    }

    // StaticJsonDocument meant for sending data <1kB
    // 200 bytes expected to send = 200 ASCII characters
    StaticJsonDocument<capacity> data;
    data["latitude"] = latitude;
    data["longitude"] = longitude;
    data["date"] = dat;
    data["time"] = tim; 
    serializeJson(data, Serial);

    delay(500);
  }
}
