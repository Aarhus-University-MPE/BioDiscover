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

// New camera_30088089
// Old camera1_23466452
// Old camera2_23466451
// Old camera1.2_23734553
// Old camera2.2_23466442
// #define CAM_ID1           30088089        // ID for camera 1
#define CAM_ID1           23734553        // ID for camera 1
#define CAM_ID2           23466442        // ID for camera 2
#define SYS_SERIAL        "1.5XL-01-03.25"  // System Serial Number (Version-Increment-Prod_Month.Prod_year)
#define Identification    "F2"              // Identification

// Request ID's       
#define CMD_Ident         201  // Request ID for Identification
#define CMD_CLOSE         101  // Start Closing maneuver
#define CMD_OPEN          102  // Start Opening maneuver
#define CMD_POS           104  // Report Position
#define CMD_URlow         105  // Send URSignal
#define CMD_URhigh        106  // Send URSignal
#define CMD_SERIAL        107  // Report System Serial number
#define CMD_CAM1          108  // Report Camera 1 ID
#define CMD_CAM2          109  // Report Camera 2 ID

#define STDBY             0
#define CLOSE             1
#define OPEN              2

#define PIN_D9            9
#define PIN_D10          10
#define PIN_D11          11
#define PIN_D12          12
#define PIN_D13          13

int MODE                 = STDBY;  // Current MODE (Standby (0), OPEN (1) or CLOSE (2))
unsigned long delayStart = 0;      // the time the delay started
int POS                  = STDBY;  // Current Positionint
int Cnt                  = 0; 
int URPOS                = LOW;    // Current URSignal

// Pinout
const int Valve_Close = PIN_D9;
const int Valve_Open  = PIN_D10;
const int URSignal    = PIN_D11;

//--------------------------------------//
//                SETUP                 //
//--------------------------------------//

void valveClose(){
  if (digitalRead (Valve_Open) == HIGH) {
      digitalWrite(Valve_Open, LOW);
      delay(100);
      }

    digitalWrite(Valve_Close, HIGH);
    delay(100);
    digitalWrite(Valve_Close, LOW);
    MODE = STDBY;
    POS  = CLOSE;
}
void valveOpen(){
      if (digitalRead (Valve_Close) == HIGH) {
      digitalWrite(Valve_Close, LOW);
      delay(100);
      }

    digitalWrite(Valve_Open, HIGH);
    delay(100);
    digitalWrite(Valve_Open, LOW);
    MODE = STDBY;
    POS  = OPEN;}


void setup() {
  pinMode(Valve_Close, OUTPUT);
  pinMode(Valve_Open, OUTPUT);

  digitalWrite(Valve_Close, LOW);
  digitalWrite(Valve_Open, LOW);
  delay(100);
  digitalWrite(Valve_Close, HIGH);
  delay(100);
  digitalWrite(Valve_Close, LOW);
  POS = CLOSE;

  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect.
  }
}

void URlow(){
  digitalWrite(URSignal, LOW);
  URPOS = LOW;
}

void URhigh(){
  digitalWrite(URSignal, HIGH);
  URPOS = HIGH;
}

//--------------------------------------//
//                MAIN                  //
//--------------------------------------//

void loop() {
  // Cnt = Cnt + 1;
  //------------Linear Actuator Mode------------//
  //--------------------------------------------//

  // Closing

  // Opening

  //------------------Commands------------------//
  //--------------------------------------------//

  if (Serial.available()) {
    int CMD = Serial.parseInt();

    switch (CMD) {
      case CMD_Ident:
        Serial.println(Identification);
        break;
      case CMD_CLOSE:
        MODE = CLOSE;
        valveClose();
        break;
      case CMD_OPEN:
        MODE = OPEN;
        valveOpen();
        break;
      case CMD_POS:
        Serial.println(POS);
        break;
      case CMD_SERIAL:
        Serial.println(SYS_SERIAL);
        break;
      case CMD_URlow:
        URlow();
        Serial.println(URPOS);
        break;
      case CMD_URhigh:
        URhigh();
        Serial.println(URPOS);
        break;
      case CMD_CAM1:
        Serial.println(CAM_ID1);
        break;
      case CMD_CAM2:
        Serial.println(CAM_ID2);
        break;
      default:
        break;
    }
  }
  // Serial.println(Cnt);  Check speed of loop
}
