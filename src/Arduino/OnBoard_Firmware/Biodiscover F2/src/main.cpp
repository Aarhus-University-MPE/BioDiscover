/*
    Description

    By
    Mads Rosenhoej Jeppesen - Aarhus 2019
    mrj@mpe.au.dk

    Later Eddited [for versions 1.4 and up] By
    Jeppe Fogh Rasmussen - Aarhus 2024
    jfr@mpe.au.dk

    Version update:
    - Implementation of Camera ID, store and request
    - 31/03/22 Added System Serial, store and request
*/

//--------------------------------------//
//              Initialize              //
//--------------------------------------//

#include <Arduino.h>

#define CAM_ID1           11111111        // ID for camera 1
#define CAM_ID2           40462643        // ID for camera 2
#define SYS_SERIAL        "1.4-01-11.24"  // System Serial Number (Version-Increment-Prod_Month.Prod_year)

// Request ID's
#define CMD_CLOSE         101  // Start Closing maneuver
#define CMD_OPEN          102  // Start Opening maneuver
#define CMD_POS           104  // Report Position
#define CMD_SERIAL        107  // Report System Serial number
#define CMD_CAM1          108  // Report Camera 1 ID
#define CMD_CAM2          109  // Report Camera 2 ID
#define CMD_CLOSE_MNL     111  // Manual Close (50 ms)
#define CMD_OPEN_MNL      112  // Manual Open (50 ms)

#define STDBY             0
#define CLOSE             1
#define OPEN              2

#define PIN_D9            9
#define PIN_D10          10
#define PIN_D11          11
#define PIN_D12          12
#define PIN_D13          13


#define VALVE_OPEN        HIGH  // Extend
#define VALVE_CLOSE       LOW   // Retract

int MODE                 = STDBY;  // Current MODE (Standby (0), OPEN (1) or CLOSE (2))
unsigned long delayStart = 0;      // the time the delay started
int POS                  = STDBY;      // Current Position


// Pinout
const int Valve_Close = PIN_D9;
const int Valve_Open  = PIN_D10;

//--------------------------------------//
//                SETUP                 //
//--------------------------------------//

void setup() {
  pinMode(Valve_Close, OUTPUT);
  pinMode(Valve_Open, OUTPUT);

  digitalWrite(Valve_Close, LOW);
  digitalWrite(Valve_Open, LOW);
  delay(50);
  digitalWrite(Valve_Close, HIGH);
  delay(50);
  digitalWrite(Valve_Close, LOW);
  POS = CLOSE;

  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect.
  }
}

//--------------------------------------//
//                MAIN                  //
//--------------------------------------//

void loop() {

  //------------Linear Actuator Mode------------//
  //--------------------------------------------//

  // Closing
  if (MODE == CLOSE) {
    if (digitalRead (Valve_Open) == HIGH) {
      digitalWrite(Valve_Open, LOW);
      delay(50);
      }

    digitalWrite(Valve_Close, HIGH);
    delay(50);
    digitalWrite(Valve_Close, LOW);
    MODE = STDBY;
    POS  = CLOSE;
    //Serial.println("CLOSE");  // Close Complete (Can only be active when testing with direct serial not labview)
  }

  // Opening
  else if (MODE == OPEN) {
    if (digitalRead (Valve_Close) == HIGH) {
      digitalWrite(Valve_Close, LOW);
      delay(50);
      }

    digitalWrite(Valve_Open, HIGH);
    delay(50);
    digitalWrite(Valve_Open, LOW);
    MODE = STDBY;
    POS  = OPEN;
    //Serial.println("OPEN");  // Open Complete (Can only be active when testing with direct serial not labview)
  }

  //------------------Commands------------------//
  //--------------------------------------------//

  if (Serial.available()) {
    int CMD = Serial.parseInt();

    switch (CMD) {
      case CMD_CLOSE:
        MODE = CLOSE;
        delayStart = millis();
        break;
      case CMD_OPEN:
        MODE = OPEN;
        delayStart = millis();
        break;
      case CMD_POS:
        Serial.println(POS);
        break;
      case CMD_SERIAL:
        Serial.println(SYS_SERIAL);
        break;
      case CMD_CAM1:
        Serial.println(CAM_ID1);
        break;
      case CMD_CAM2:
        Serial.println(CAM_ID2);
        break;
      case CMD_CLOSE_MNL:
       MODE = CLOSE;
       delayStart = millis();
        break;
      case CMD_OPEN_MNL:
        MODE = OPEN;
        delayStart = millis();
        break;
      default:
        break;
    }
  }
}
