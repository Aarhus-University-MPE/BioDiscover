/*
    Description

    By
    Mads Rosenhoej Jeppesen - Aarhus 2019
    mrj@mpe.au.dk

    Version update:
    Implementation of Camera ID, stored and request
*/

//--------------------------------------//
//              Initialize              //
//--------------------------------------//

#define CAM_ID1       23466452          // ID for camera 1        
#define CAM_ID2       23466451          // ID for camera 2

#define PIN_D5        5
#define PIN_D6        6
#define PIN_D7        7
#define PIN_D8        8
#define PIN_D9        9
#define PIN_D10       10

#define STDBY         0
#define OPEN          1
#define CLOSE         2

#define VALVE_OPEN    HIGH              // Extend
#define VALVE_CLOSE   LOW               // Retract

int MODE = STDBY;                       // Current MODE (Standby (0), OPEN (1) or CLOSE (2))
unsigned long delayStart = 0;           // the time the delay started

const int manual_dur = 3000;            // Manual actuator duration [ms]
const int Safety_Duration = 6000;       // Actuator safety duration [ms]
const int RTRCT_Pos = 220;
const int EXTND_Pos = 525;

const int HB_ENABLE = PIN_D5;
const int HB_DIR2   = PIN_D6;
const int HB_DIR1   = PIN_D7;
const int ACT_POS   = PIN_A0;

//--------------------------------------//
//                SETUP                 //
//--------------------------------------//

void setup() {
  digitalWrite(HB_ENABLE, LOW);
  digitalWrite(HB_DIR1, VALVE_CLOSE);
  digitalWrite(HB_DIR2, !VALVE_CLOSE);
  pinMode(HB_ENABLE, OUTPUT);
  pinMode(HB_DIR1, OUTPUT);
  pinMode(HB_DIR2, OUTPUT);
  pinMode(ACT_POS, INPUT);

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect.
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
      valve(VALVE_CLOSE, LOW);
      delay(50);
      POS = analogRead(ACT_POS);
      if (POS >= RTRCT_Pos && ((millis() - delayStart) <= Safety_Duration)) {
        valve(VALVE_CLOSE, HIGH);
        delay(50);
      }
      else {
        MODE = STDBY;
        Serial.println(2);      // Close Complete
      }
    }
  }

  // Opening
  else if (MODE == OPEN)
  {
    if (POS >= EXTND_Pos || ((millis() - delayStart) >= Safety_Duration))   // Endstop reached or timeout
    {
      valve(VALVE_OPEN, LOW);
      delay(50);
      POS = analogRead(ACT_POS);
      if (POS <= EXTND_Pos && ((millis() - delayStart) <= Safety_Duration)) {
        valve(VALVE_OPEN, HIGH);
      }
      else {
        MODE = STDBY;
        Serial.println(1);      // Open Complete
      }
    }
  }

  //------------------Commands------------------//
  //--------------------------------------------//

  if (Serial.available()) {
    int CMD = Serial.parseInt();

    // Close
    if (CMD == 101)
    {
      MODE = CLOSE;
      valve(VALVE_CLOSE, HIGH);
      delayStart = millis();
    }

    // Open
    else if (CMD == 102)
    {
      MODE = OPEN;
      valve(VALVE_OPEN, HIGH);
      delayStart = millis();
    }

//    // Full cycle
//    else if (CMD == 103)
//    {
//      MODE = 2;
//      command(DIR, ACT);
//      delayStart = millis();
//    }

    // Send Position data
    else if (CMD == 104)
    {
      Serial.println(POS);
    }

    // CAM ID 1
    else if (CMD == 108)
    {
      Serial.println(CAM_ID1);
    }

    // CAM ID 2
    else if (CMD == 109)
    {
      Serial.println(CAM_ID2);
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
