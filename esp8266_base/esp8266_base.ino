#include <DHTesp.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const int dhtPin = 14;
const char* ssid = ""; // Add network ID
const char* password = ""; // Add password
const char* http_server = "http://"; // Add server IP address

DHTesp dht;
HTTPClient http;

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

  if(WiFi.status()== WL_CONNECTED){
    http.begin(http_server);
    http.addHeader("Content-Type", "application/json");
 
    int httpResponseCode = http.POST("{\"temperature\":temperature,\"humidity\":humidity}");
    #int httpResponseCode = http.POST("Putting data");
    if(httpResponseCode>0){
      // handle server response
    }
  
    String response = http.getString();
 
    Serial.println(httpResponseCode);
    Serial.println(response);

    http.end();
  }

  Serial.print("Status = "); Serial.print(dht.getStatusString());
  Serial.print("\t Temperature = "); Serial.print(temperature, 1);
  Serial.print("\t Humidity = "); Serial.println(humidity, 1);
  delay(60 * 1000);
}

