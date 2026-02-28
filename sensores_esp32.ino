#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>
#define ssid  "RODOLFO"
#define password "rodolfoC123"
//const char* serverName = "http://127.0.0.1:8000/api/leituras/";
//const char* serverName = "http://192.168.1.197:8000/api/leituras/";
const char* serverName = "https://iot-cc0r.onrender.com/api/leituras/";




void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println(WiFi.status());
    Serial.print('a');
    delay(1000);
  }
  Serial.println("Connected");
  Serial.println("Status: ");
  Serial.println(WiFi.status());
  Serial.println("Local IP : ");
  Serial.println(WiFi.localIP());
  Serial.print("RRSI: ");
  Serial.println(WiFi.RSSI());
  Serial.println("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  Serial.println("SubnetMask: ");
  Serial.println(WiFi.subnetMask());
}


void setup() {
  Serial.begin(115200);
  //Serial.println("Opa");
  initWiFi();
}

void loop() {
  WiFiClientSecure client;
  client.setInsecure();  // para ignorar certificado
  if (WiFi.status() == WL_CONNECTED) {
    //Serial.println("Conectado com sucesso!");
    HTTPClient http;
    http.setTimeout(20000);  // 20 segundos
    http.begin(client,serverName);
    http.addHeader("Content-Type", "application/json");

    float s1 = random(0,100);
    float s2 = random(0,100);
    float s3 = random(0,100);
    float s4 = random(0,100);
    float s5 = random(0,100);
    float s6 = random(0,100);

    String json = "{";
    json += "\"sensor_1\":" + String(s1) + ",";
    json += "\"sensor_2\":" + String(s2) + ",";
    json += "\"sensor_3\":" + String(s3) + ",";
    json += "\"sensor_4\":" + String(s4) + ",";
    json += "\"sensor_5\":" + String(s5) + ",";
    json += "\"sensor_6\":" + String(s6);
    json += "}";
    //Serial.print("JSON:");
    //Serial.println(json);
    //delay(3000);
    //int response = http.POST(json);
    int response = http.sendRequest("POST",json);
    Serial.print("Response : ");
    Serial.println(response);

    http.end();
  }
  else{
    Serial.println("Erro wifi!");
  }

  delay(5000); // a cada cinco minutos
}