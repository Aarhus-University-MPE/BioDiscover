#include <Arduino.h>

const int fanPWM = 11;  // Pin D11 (OC2A)
int speedPercent = 0;

// Fan's effective control range
const int minDuty = 102;  // ~40% of 255
const int maxDuty = 204;  // ~80% of 255

void analogWriteMapped(int percent);

// Map 0–100% input to minDuty–maxDuty PWM range
void analogWriteMapped(int percent) {
  if (percent <= 0) {
    OCR2A = 0;  // Fully off
  } else {
    OCR2A = map(percent, 0, 100, minDuty, maxDuty);
  }
}

void setup() {
  Serial.begin(9600);
  Serial.println("Enter fan speed (0>100%):");

  // Set up Timer2 for ~25kHz PWM on pin 11
  pinMode(fanPWM, OUTPUT);

  TCCR2A = 0;
  TCCR2B = 0;
  TCNT2  = 0;

  TCCR2A |= (1 << WGM20) | (1 << WGM21); // Fast PWM
  TCCR2A |= (1 << COM2A1);               // Non-inverting mode on OC2A (Pin 11)
  TCCR2B |= (1 << CS20);                 // No prescaling → 25kHz PWM

  analogWriteMapped(0);  // Initialize fan at minimum usable speed
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    int percent = input.toInt();

    if (percent >= 0 && percent <= 100) {
      speedPercent = percent;
      analogWriteMapped(speedPercent);
      Serial.print("Fan speed set to ");
      Serial.print(speedPercent);
      Serial.println("% (mapped to PWM)");
    } else {
      Serial.println("Please enter a number between 0 and 100.");
    }
  }
}