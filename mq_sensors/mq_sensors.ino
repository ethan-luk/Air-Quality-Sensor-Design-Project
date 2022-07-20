#include <ArduinoJson.h>
#include <Wire.h> 
#include <MQUnifiedsensor.h>


/***
 * Technical documentation:
 * https://jayconsystems.com/blog/understanding-a-gas-sensor
*/

// #define Capacity JSON_OBJECT_SIZE(11)

#define Board ("Arduino UNO")
#define PinMQ3 (A0)
#define PinMQ4 (A1)
#define PinMQ135 (A2)
#define PinMQ7 (A3)
#define PinMQ9 (A7)


/***Each ratio is defined by: RS/R0
 * RS/R0 is the resistance ratio of the sensor, which gives concentration of a gas in ppm (parts per million)
 * 
 * where RS = resistance of the sensor that changes depending on concentration of gas
 *       R0 = resistance of sensor in fresh air
 * >>> sensors need to be calibrated to determine R0      
 */
#define RatioMQ3CleanAir (60)
#define RatioMQ4CleanAir  (4.4)
#define RatioMQ135CleanAir (3.6)
#define RatioMQ7CleanAir (27.5)
#define RatioMQ9CleanAir (9.6)


#define ADC_Bit_Resolution (10)  // 10 bit ADC 
#define Voltage_Resolution (5)  // Volt resolution to calc the voltage
#define Type ("Arduino UNO")

//Declare Sensor objects
MQUnifiedsensor MQ3(Board, Voltage_Resolution, ADC_Bit_Resolution, PinMQ3, Type);
MQUnifiedsensor MQ4(Board, Voltage_Resolution, ADC_Bit_Resolution, PinMQ4, Type);
MQUnifiedsensor MQ135(Board, Voltage_Resolution, ADC_Bit_Resolution, PinMQ135, Type);
MQUnifiedsensor MQ7(Board, Voltage_Resolution, ADC_Bit_Resolution, PinMQ7, Type);
MQUnifiedsensor MQ9(Board, Voltage_Resolution, ADC_Bit_Resolution, PinMQ9, Type);


void setup() {
  Serial.begin(9600);                


// IMPORTANT: update the values of R0 for each sensor once they've been determined from calibration and uncomment once you're done with calibration
  MQ3.init();
  MQ3.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ3.setR0(0.17);
  MQ4.init();
  MQ4.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ4.setR0(3.79);
  MQ135.init();
  MQ135.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ135.setR0(5.10);
  MQ7.init();
  MQ7.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ7.setR0(0.24);
  MQ9.init();
  MQ9.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ9.setR0(0.73);


/***
 * MQ SENSOR CALIBRATION --- DETERMINING R0 VALUE FOR EACH SENSOR
 * Comment this portion when done with calibration
 */

//  Serial.print("Calibrating please wait.");
//  float  MQ3calcR0 = 0,
//         MQ4calcR0 = 0,
//         MQ135calcR0 = 0,
//         MQ7calcR0 = 0,
//         MQ9calcR0 = 0;
//         
//  for (int i = 1; i <= 100; i ++){
//    //Update the voltage lectures
//    MQ3.update();
//    MQ4.update();
//    MQ135.update();
//    MQ7.update();
//    MQ9.update();
//
//    MQ3calcR0 += MQ3.calibrate(RatioMQ3CleanAir);
//    MQ4calcR0 += MQ4.calibrate(RatioMQ4CleanAir);
//    MQ135calcR0 += MQ135.calibrate(RatioMQ135CleanAir);
//    MQ7calcR0 += MQ7.calibrate(RatioMQ7CleanAir);
//    MQ9calcR0 += MQ9.calibrate(RatioMQ9CleanAir);
//
//    Serial.print(".");
//  }
//  
//  MQ3.setR0(MQ3calcR0 / 100);
//  MQ4.setR0(MQ4calcR0 / 100);
//  MQ135.setR0(MQ135calcR0 / 100);
//  MQ7.setR0(MQ7calcR0 / 100);
//  MQ9.setR0(MQ9calcR0 / 100);
//  Serial.println("  done!.");
//
//  Serial.print("(MQ3 to MQ9):");
//  Serial.print(MQ3calcR0 / 100); Serial.print(" | ");
//  Serial.print(MQ4calcR0 / 100); Serial.print(" | ");
//  Serial.print(MQ135calcR0 / 100); Serial.print(" | ");
//  Serial.print(MQ7calcR0 / 100); Serial.print(" | ");
//  Serial.print(MQ9calcR0 / 100); Serial.println(" |");

  /*****************************  End of MQ Sensor Calibration ********************************************/ 
}


void loop() {
  
  //Update data
  MQ3.update();
  MQ4.update();
  MQ135.update();  
  MQ7.update();
  MQ9.update();


  MQ3.setA(0.3934); MQ3.setB(-1.504); //Alcohol
  float Alcohol = MQ3.readSensor(); 

  MQ3.setA(4.8387); MQ3.setB(-2.68); //Benzene
  float Benzene = MQ3.readSensor(); 
  
  MQ3.setA(7585.3); MQ3.setB(-2.849); //Hexane
  float Hexane = MQ3.readSensor(); 

  MQ4.setA(1012.7); MQ4.setB(-2.786); //CH4
  float CH4 = MQ4.readSensor(); 

  MQ4.setA(30000000); MQ4.setB(-8.308); //smoke 
  float Smoke = MQ4.readSensor(); 
 
  MQ135.setA(110.47); MQ135.setB(-2.862); //CO2 
  float CO2 = MQ135.readSensor(); 
  CO2 = CO2*100;
  
  MQ135.setA(44.947); MQ135.setB(-3.445); // Toluene
  float Toluene = MQ135.readSensor(); 
  
  MQ135.setA(102.2 ); MQ135.setB(-2.473); //NH4 
  float NH4 = MQ135.readSensor(); 
  
  MQ135.setA(34.668); MQ135.setB(-3.369); //Acetone
  float Acetone = MQ135.readSensor(); 
 
  MQ7.setA(99.042); MQ7.setB(-1.518); //CO
  float CO = MQ7.readSensor(); 

  MQ9.setA(1000.5); MQ9.setB(-2.186); //flammable gas
  float FG = MQ9.readSensor();



//  Serial.print("Alcohol:  "); Serial.println(Alcohol);
//  Serial.print("Benzene:  "); Serial.println(Benzene);
//  Serial.print("Hexane:   "); Serial.println(Hexane);
//  Serial.print("Methane:  "); Serial.println(CH4);
//  Serial.print("Smoke:    "); Serial.println(Smoke);
//  Serial.print("CO2:      "); Serial.println(CO2);
//  Serial.print("Toluene:  "); Serial.println(Toluene);
//  Serial.print("NH4:      "); Serial.println(NH4);
//  Serial.print("Acetone:  "); Serial.println(Acetone);  
//  Serial.print("CO:       "); Serial.println(CO);
//  Serial.print("FG:       "); Serial.println(FG);
//  Serial.println("--------------------------------------------------------");
//  delay(1000);
  
  float data[11] = {Alcohol, Benzene, Hexane, CH4, Smoke, CO2, Toluene, NH4, Acetone, CO, FG};
  int len = (sizeof(data)-sizeof(data[0]))/sizeof(data[0]);

  for (int i = 0; i < len; i++) {
    Serial.print(data[i], 6);
    Serial.print(", ");
  }
  Serial.print(data[10], 6);
  Serial.println();
  delay(1000);


     
//  StaticJsonDocument<300> data;
//  data["alcohol"] = Alcohol;
//  data["benzene"] = Benzene;
//  data["hexane"] = Hexane;
//  data["ch4"] = CH4;
//  data["smoke"] = Smoke;
//  data["co2"] = CO2;
//  data["toluene"] = Toluene;
//  data["nh4"] = NH4;
//  data["acetone"] = Acetone;
//  data["co"] = CO;
//  data["fg"] = FG;
//  serializeJson(data, Serial);
//  Serial.println();
//  delay(5000);
  

}
