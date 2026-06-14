#include <WiFi.h>
#include <WiFiClient.h>
#define PIN_TRIG      5
#define PIN_ECHO      18
#define PIN_BUZZER    19
#define PIN_LED_GREEN 21
#define PIN_LED_AMBER 22
#define PIN_LED_RED   23
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
const char* TS_HOST = "api.thingspeak.com";
String TS_WRITE_API_KEY = "YOUR_THINGSPEAK_WRITE_KEY";
const float BIN_MAX_HEIGHT_CM = 50.0;
unsigned long lastTransmissionTime = 0;
WiFiClient networkClient;
void setup() {
  Serial.begin(115200);
  pinMode(PIN_TRIG, OUTPUT); pinMode(PIN_ECHO, INPUT);
  pinMode(PIN_BUZZER, OUTPUT); pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_AMBER, OUTPUT); pinMode(PIN_LED_RED, OUTPUT);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}
void loop() {
  digitalWrite(PIN_TRIG, LOW); delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);
  long duration = pulseIn(PIN_ECHO, HIGH, 30000);
  float distance = (float)duration * 0.0343 / 2.0;
  if (distance > BIN_MAX_HEIGHT_CM || distance <= 0) distance = BIN_MAX_HEIGHT_CM;
  float fillPercentage = ((BIN_MAX_HEIGHT_CM - distance) / BIN_MAX_HEIGHT_CM) * 100.0;
  if (fillPercentage >= 80.0) {
    digitalWrite(PIN_LED_RED, HIGH); digitalWrite(PIN_BUZZER, HIGH);
  } else if (fillPercentage >= 50.0) {
    digitalWrite(PIN_LED_AMBER, HIGH);
  } else {
    digitalWrite(PIN_LED_GREEN, HIGH);
  }
  delay(1000);
}