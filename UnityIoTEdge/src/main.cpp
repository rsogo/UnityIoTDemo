#include <M5Core2.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "dummy";                               // WiFiのSSID
const char *password = "dummy";                       // WiFiのパスワード
const char *serverAddress = "http://dummy:8000/sensor/1"; // APIのエンドポイント

void setup()
{
    M5.begin();               // Init M5Core2.  初始化 M5Core2
    Serial.begin(9600);
    
    delay(1000);

    // WiFiへ接続
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.println("Connecting to WiFi..." + WiFi.status());
        delay(1000);
    }
    Serial.println("Connected to WiFi");
}

// センサーデータをPOSTする
void postData(float sensorData)
{
    HTTPClient http;
    http.begin(serverAddress);

    // Content-TypeをJSON形式に設定
    http.addHeader("Content-Type", "application/json");

    // POSTするJSONデータを設定
    String jsonData = "{\"sensor_data\":" + String(sensorData) + "}";

    Serial.println("JSON data: " + jsonData);
    int httpResponseCode = http.POST(jsonData);
    // int httpResponseCode = http.GET();

    // レスポンスのコードを表示
    Serial.println("HTTP response code: " + String(httpResponseCode));

    http.end();
}

void loop()
{

    M5.update(); // Read the press state of the key.  读取按键 A, B, C 的状态

    delay(5000);
    postData(1.0);
}

