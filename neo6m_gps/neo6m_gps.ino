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
double latitude, longitude;
uint32_t dat, tim;

// instantiating objects
TinyGPSPlus gps; 
SoftwareSerial mySerial = SoftwareSerial(RXPin,TXPin);

void setup() {
  pinMode(RXPin, INPUT);
  pinMode(TXPin, OUTPUT);  
  Serial.begin(9600);
  mySerial.begin(GPSBaud);
}

void loop() {
  
  // .available() returns number of bytes ready to read
  while (mySerial.available() > 0) {  
    gps.encode(mySerial.read());
    
//    if (gps.location.isUpdated()){
//      latitude = gps.location.lat();  // type double
//      longitude = gps.location.lng(); // type double
//
//      dat = gps.date.value(); // type unsigned 32 bit int
//      tim = gps.time.value(); // type unsigned 32 bit int
//    }


      // important values without checking isUpdated()
      latitude = gps.location.lat();  // type double
      longitude = gps.location.lng(); // type double
      dat = gps.date.value(); // type unsigned 32 bit int
      tim = gps.time.value(); // type unsigned 32 bit int



//  if (millis() > 5000 && gps.charsProcessed() < 10) { // uh oh
//    Serial.println("ERROR: not getting any GPS data!");
//    // dump the stream to Serial
//    Serial.println("GPS stream dump:");
//    while (true) // infinite loop
//      if (ss.available() > 0) // any data coming in?
//        Serial.write(ss.read());
//    }


    // StaticJsonDocument meant for sending data <1kB
    // 200 bytes expected to send = 200 ASCII characters
//    StaticJsonDocument<capacity> data;
//    data["latitude"] = latitude;
//    data["longitude"] = longitude;
//    data["date"] = dat;
//    data["time"] = tim; 
//    serializeJson(data, Serial);
//    Serial.println();

    delay(500);
  }
  Serial.println("hi");
}
