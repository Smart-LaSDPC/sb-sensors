#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT22 

#define temp_low 5
#define temp_high 19
#define temp_ok 21

#define humidity_low 23
#define humidity_ok 15
#define humidity_high 16

DHT dht(DHTPIN, DHTTYPE);

void setup() {
 Serial.begin(9600);
 Serial.println();

 dht.begin();

//temperatura

pinMode(temp_low,OUTPUT);
pinMode(temp_high,OUTPUT);
pinMode(temp_ok,OUTPUT);

//humidity

pinMode(humidity_low,OUTPUT);
pinMode(humidity_high,OUTPUT);
pinMode(humidity_ok,OUTPUT);

}

void loop() {
 delay(1000);
 float h = dht.readHumidity();
 float t = dht.readTemperature();

 Serial.print("Humidity: ");
 Serial.print(h);
 Serial.print(" %\t");
 Serial.print("Temperature: ");
 Serial.print(t);
 Serial.println(" °C");

 //bloco de temperatura
 
 if (t < 21.5){
  digitalWrite(temp_low,HIGH);
  digitalWrite(temp_high,LOW);
  digitalWrite(temp_ok,LOW);
 }
 if (t > 22.5) {
  digitalWrite(temp_high,HIGH);
  digitalWrite(temp_low,LOW);
  digitalWrite(temp_ok,LOW);
 }
 if (t > 21.6 or t < 22.4){
  digitalWrite(temp_high,LOW);
  digitalWrite(temp_low,LOW);
  digitalWrite(temp_ok,HIGH);
 }

//bloco de humidade

 if (h < 40.0) {
  digitalWrite(humidity_high,HIGH);
  digitalWrite(humidity_low,LOW);
  digitalWrite(humidity_ok,LOW);
 }
if (h > 40.0 or h < 70.0){
digitalWrite(humidity_high,LOW);
digitalWrite(humidity_low,LOW);
digitalWrite(humidity_ok,HIGH);
}
if (h > 70.0){
digitalWrite(humidity_high,HIGH);
digitalWrite(humidity_low,LOW);
digitalWrite(humidity_ok,LOW);
}
}
