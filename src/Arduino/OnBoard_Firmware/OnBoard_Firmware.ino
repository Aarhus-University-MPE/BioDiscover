
/*
    Description

    By
    Mads Rosenhoej Jeppesen - Aarhus 2019
    mrj@mpe.au.dk

    Version update:
    - Implementation of Camera ID, store and request
    - 31/03/22 Added System Serial, store and request
*/

//--------------------------------------//
//              Initialize              //
//--------------------------------------//

#define CAM_ID1           23466443          // ID for camera 1
#define CAM_ID2           23466444          // ID for camera 2
#define SYS_SERIAL        "1.2XL-02-05.21"  // System Serial Number (Version-Increment-Prod_Month.Prod_year)

// Request ID's
#define CMD_CLOSE         101  // Start Closing maneuver
#define CMD_OPEN          102  // Start Opening maneuver
#define CMD_POS           104  // Report Position
#define CMD_SERIAL        107  // Report System Serial number
#define CMD_CAM1          108  // Report Camera 1 ID
#define CMD_CAM2          109  // Report Camera 2 ID
#define CMD_CLOSE_MNL     111  // Manual Close (50 ms)
#define CMD_OPEN_MNL      112  // Manual Open (50 ms)
#define CMD_REQ_RTRCT_POS 121  // Request retracted position (fully closed)
#define CMD_REQ_EXTND_POS 122  // Request extended position (fully open)

#define PIN_D5            5
#define PIN_D6            6
#define PIN_D7            7
#define PIN_D8            8
#define PIN_D9            9
#define PIN_D10           10

#define STDBY             0
#define OPEN              1
#define CLOSE             2

#define VALVE_OPEN        HIGH  // Extend
#define VALVE_CLOSE       LOW   // Retract

int MODE                 = STDBY;  // Current MODE (Standby (0), OPEN (1) or CLOSE (2))
unsigned long delayStart = 0;      // the time the delay started

const int manual_dur      = 3000;  // Manual actuator duration [ms]
const int Safety_Duration = 6000;  // Actuator safety duration [ms]

const int RTRCT_Pos = 215;  // End position
const int EXTND_Pos = 835;  // End position

// Pinout
const int HB_ENABLE = PIN_D5;
const int HB_DIR2   = PIN_D6;
const int HB_DIR1   = PIN_D7;
const int ACT_POS   = A0;

//--------------------------------------//
//                SETUP                 //
//--------------------------------------//

void setup() {
  pinMode(HB_ENABLE, OUTPUT);
  pinMode(HB_DIR1, OUTPUT);
  pinMode(HB_DIR2, OUTPUT);
  digitalWrite(HB_ENABLE, LOW);
  digitalWrite(HB_DIR1, LOW);
  digitalWrite(HB_DIR2, LOW);
  pinMode(ACT_POS, INPUT);

  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect.
  }
}

//--------------------------------------//
//                MAIN                  //
//--------------------------------------//

void loop() {
  int POS = analogRead(ACT_POS);

  //------------Linear Actuator Mode------------//
  //--------------------------------------------//

  // Closing
  if (MODE == CLOSE) {
    if (POS <= RTRCT_Pos || ((millis() - delayStart) >= Safety_Duration))  // Endstop reached or timeout
    {
      (VALVE_CLOSE, LOW);
      delay(50);
      POS = analogRead(ACT_POS);
      if (POS >= RTRCT_Pos && ((millis() - delayStart) <= Safety_Duration)) {
        valve(VALVE_CLOSE, HIGH);
        delay(50);
      } else {
        MODE = STDBY;
        Serial.println(2);  // Close Complete
      }
    }
  }

  // Opening
  else if (MODE == OPEN) {
    if (POS >= EXTND_Pos || ((millis() - delayStart) >= Safety_Duration))  // Endstop reached or timeout
    {
      valve(VALVE_OPEN, LOW);
      delay(50);
      POS = analogRead(ACT_POS);
      if (POS <= EXTND_Pos && ((millis() - delayStart) <= Safety_Duration)) {
        valve(VALVE_OPEN, HIGH);
      } else {
        MODE = STDBY;
        Serial.println(1);  // Open Complete
      }
    }
  } else {
    valveStop();
  }

  //------------------Commands------------------//
  //--------------------------------------------//

  if (Serial.available()) {
    int CMD = Serial.parseInt();

    switch (CMD) {
      case CMD_CLOSE:
        MODE = CLOSE;
        valve(VALVE_CLOSE, HIGH);
        delayStart = millis();
        break;
      case CMD_OPEN:
        MODE = OPEN;
        valve(VALVE_OPEN, HIGH);
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
        Serial.println("Closing for 50 ms");
        valve(VALVE_CLOSE, HIGH);
        delay(50);
        valve(VALVE_CLOSE, LOW);
        Serial.println("Done");
        break;
      case CMD_OPEN_MNL:
        Serial.println("Opening for 50 ms");
        valve(VALVE_OPEN, HIGH);
        delay(50);
        valve(VALVE_OPEN, LOW);
        Serial.println("Done");
        break;
      case CMD_REQ_RTRCT_POS:
        Serial.println(RTRCT_Pos);
        break;
      case CMD_REQ_EXTND_POS:
        Serial.println(EXTND_Pos);
        break;

      default:
        break;
    }
  }
}

//----------------------------------------//
//              Motor Control             //
//----------------------------------------//

void valve(bool DIR, bool ACT) {
  digitalWrite(HB_ENABLE, ACT);
  digitalWrite(HB_DIR1, DIR);
  digitalWrite(HB_DIR2, !DIR);
}

void valveStop() {
  digitalWrite(HB_ENABLE, LOW);
  digitalWrite(HB_DIR1, LOW);
  digitalWrite(HB_DIR2, LOW);
}
