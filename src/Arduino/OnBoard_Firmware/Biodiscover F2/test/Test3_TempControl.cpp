#include <OneWire.h>
#include <DallasTemperature.h>

// --- Pin Definitions ---
const int oneWireBus = 12;      // DS18B20 data pin (D4)
const int fanPWM = 11;         // PWM output pin for fan

// --- Fan PWM Limits ---
const int minDuty = 76;       // ~30% duty (fan lowest usable)
const int maxDuty = 230;       // ~90% duty (fan max)
const float minTemp = 25.0;    // Start ramping at this temp
const float maxTemp = 85.0;    // Full speed at this temp

// --- 1-Wire Setup ---
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

// --- State ---
bool autoMode = false;
int manualPercent = 0;

// CAlling functions
void analogWriteMapped(int percent);
int calculateFanPWM(float temp);

void setup() {
  Serial.begin(9600);
  sensors.begin();
  pinMode(fanPWM, OUTPUT);

  // Timer2 setup for 25kHz PWM on Pin 11
  TCCR2A = 0;
  TCCR2B = 0;
  TCNT2  = 0;
  TCCR2A |= (1 << WGM20) | (1 << WGM21); // Fast PWM
  TCCR2A |= (1 << COM2A1);               // Non-inverting on OC2A
  TCCR2B |= (1 << CS20);                 // No prescaler

  analogWriteMapped(0); // Start fan off
  Serial.println("Enter 0>100 to set fan speed manually, or 'a' for auto mode.");
}

void loop() {
  // Read from Serial
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input.equalsIgnoreCase("a")) {
      autoMode = true;
      Serial.println("Switched to AUTOMATIC mode.");
    } else {
      int value = input.toInt();
      if (value >= 0 && value <= 100) {
        autoMode = false;
        manualPercent = value;
        analogWriteMapped(manualPercent);
        Serial.print("Manual mode: fan set to ");
        Serial.print(manualPercent);
        Serial.println("%");
      } else {
        Serial.println("Invalid input. Enter 0>100 or 'a'.");
      }
    }
  }

  // Auto mode logic
  if (autoMode) {
    sensors.requestTemperatures();
    float tempC = sensors.getTempCByIndex(0);

    Serial.print("Temperature: ");
    Serial.print(tempC);
    Serial.print(" °C , ");

    int pwmValue = calculateFanPWM(tempC);
    OCR2A = pwmValue;

    int effectivePercent = map(pwmValue, minDuty, maxDuty, 30, 90);
    Serial.print("Fan running at ~");
    Serial.print(effectivePercent);
    Serial.println("%");

    delay(1000); // Update every 1 sec
  }

  // Manual mode: nothing happens here – PWM already set
}

// --- PWM Duty Control ---
void analogWriteMapped(int percent) {
  if (percent <= 0) OCR2A = 0;
  else OCR2A = map(percent, 0, 100, minDuty, maxDuty);
}

// --- Temp → PWM Mapping ---
int calculateFanPWM(float temp) {
  if (temp <= minTemp) return 76;         // Fan Idle
  if (temp >= maxTemp) return maxDuty;    // Full speed
  return map((int)(temp * 10), (int)(minTemp * 10), (int)(maxTemp * 10), minDuty, maxDuty);
}
