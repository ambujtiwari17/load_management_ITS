// EmonLibrary examples openenergymonitor.org, Licence GNU GPL V3

#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon1;                   // Create an instance
double Irms = 0;
int Power = 0;
#define RELAY1  7
void setup()
{  
  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);
  digitalWrite(RELAY1,1);
  emon1.current(1, 55.1);   // Current: input pin, calibration.
  //double Irms = 0;
}

void loop()
{
  Irms = emon1.calcIrms(1480);  // Calculate Irms only
  Irms = Irms - 0.13;
  Power = (Irms*230.0)/10; 
  Serial.println(Power);	       // Apparent power
  //Serial.print(" ");
 // Serial.println(Irms);
  //delay(5000);
 if(Power > 200)
 {  //delay(500);
    digitalWrite(RELAY1,0);           // Turns ON Relays 1
    //Serial.println("Light OFF");
   // break;
 }
 
 if(Power < 130)
 {
  digitalWrite(RELAY1,1); 
  delay(5000);
 }
 //else
 //{
 // digitalWrite(RELAY1,1);
 //}
 		       // Irms
}
