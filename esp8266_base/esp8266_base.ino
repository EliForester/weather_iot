#include <DHTesp.h>
#include <ESP8266WiFi.h>

DHTesp dht;

const int dhtPin = 14;
const char* ssid = "" // Add network ID
const char* password = "" // Add password

void setup(){
  Serial.begin(115200);
  Serial.println("I'm alive!");
  
  Serial.println("Starting up DHT");
  dht.setup(dhtPin, DHTesp::DHT11);

  Serial.println("Starting up WiFi");  
  WiFi.begin(ssid, password);

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop(){
  float temperature = dht.getTemperature();
  float humidity = dht.getHumidity();

  Serial.print("Status = ");
  Serial.println(dht.getStatusString());
  Serial.print("Temperature = ");
  Serial.println(temperature, 1);
  Serial.print("Humidity = ");
  Serial.println(humidity, 1);
  delay(2000);
}
