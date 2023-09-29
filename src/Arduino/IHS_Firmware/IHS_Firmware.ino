
// In/output and variables generated from UR-robot signals.
int done = 19;                                  // Pin used for feedback to the UR-robot.
int bits0 = 15;                                 // Pin used for reading bit 0 from the UR-robot.
int bits1 = 16;                                 // Pin used for reading bit 1 from the UR-robot.
int bits2 = 17;                                 // Pin used for reading bit 2 from the UR-robot.
int bits3 = 18;                                 // Pin used for reading bit 3 from the UR-robot.
int bit_0 = 0;                                  // Bit0 is initialized and set to 0
int bit_1 = 0;                                  // Bit1 is initialized and set to 0
int bit_2 = 0;                                  // Bit2 is initialized and set to 0
int bit_3 = 0;                                  // Bit3 is initialized and set to 0

// Task system is initialized
int Task = 0;
int Task_new = 0;
int Task_old = 0;

// Last run program is initialized and set to 0
int LastRun = 0; 

// Variables for the Tool functions are initialized
int i = 0;
int Switchvardi_T = 0;

// Including the AccelStepper library:
#include <AccelStepper.h>

// Defining output pins for the two setups
#define ledPin 13                               // SMD-LED on the Arduino - used to visually tell that a loop has been completed
#define max_out 11                              // Connected to pin 11 - Input from limit switch.
#define enablePin_T 2                           // Connected to pin 2 - Enablepin on Tool stepper driver
#define dirPin_T 3                              // Connected to pin 3 - Dirpin on Tool stepper driver
#define stepPin_T 4                             // Connected to pin 4 - Steppin on Tool stepper driver

// ShakerTable
#define Reed_Switch 10                          // Connected to pin 10 - Input from Reed_Switch.
#define enablePin_S 5                           // Connected to pin 5 - Enablepin on ShakerTable stepper driver
#define dirPin_S 6                              // Connected to pin 6 - Dirpin on ShakerTable stepper driver
#define stepPin_S 7                             // Connected to pin 7 - Steppin on ShakerTable stepper driver

// Defining variables for the driver functions
int Switchvardi_S = 0;                          // Initializing readswitch readout
int cnt_S = 0;                                  // Initializing counter for finding shakertable null pos.
const int motorInterfaceType = 1;               // Tells the Accelstepper libary that it outputs to a stepper driver and not directly to a steppermotor
int microstepping_S = 1600;                     // The amount of microstepping defined on the stepperdriver for the shaker table
int microstepping_T = 800;                      // The amount of microstepping defined on the stepperdriver for the Tool 1
int surge_max_out = 0;                          // Switching variable from limit switch.

AccelStepper stepper_S = AccelStepper(motorInterfaceType, stepPin_S, dirPin_S);  //making special functions for the shaker table 
AccelStepper stepper_T = AccelStepper(motorInterfaceType, stepPin_T, dirPin_T);  //making special functions for the Tool 1

//----------------------------------------------------------------------------------------------------//

void setup() {
//Setup serial monitor.  
 Serial.begin(9600);
    
// Defining relevant pins as outputs
 pinMode(enablePin_T, OUTPUT);
 pinMode(stepPin_T, OUTPUT);
 pinMode(stepPin_T, OUTPUT);
 
 pinMode(enablePin_S, OUTPUT);
 pinMode(stepPin_S, OUTPUT);
 pinMode(stepPin_S, OUTPUT);
 
 pinMode(done, OUTPUT);
 pinMode(ledPin, OUTPUT);

// Defining relevant pins as inputs
 pinMode(bits0, INPUT);
 pinMode(bits1, INPUT);
 pinMode(bits2, INPUT);
 pinMode(bits3, INPUT);
 pinMode(max_out, INPUT);
 pinMode(Reed_Switch, INPUT);

// Setting stepperdriver to wait
 digitalWrite(enablePin_S, HIGH);
 digitalWrite(enablePin_T, HIGH);
}                                               // Closes setup
 

//----------------------------------------------------------------------------------------------------//

void loop() {
// Resetting done pin
  digitalWrite(done, LOW);
  
// Reads 4-bit signal from UR-robot.
      // bit0
      if (digitalRead(bits0) == HIGH){
       //Serial.println("bits0 = HIGH");
       bit_0 = 1;
       }
      else {
      bit_0 = 0;
      //Serial.println("bits0 = LOW");
      }
      // bit1
      if (digitalRead(bits1) == HIGH){
      //Serial.println("bits1 = HIGH");
        bit_1 = 2;
       }
       else {
      bit_1 = 0;
      //Serial.println("bits1 = LOW");
      }
      // bit2
      if (digitalRead(bits2) == HIGH){
      //Serial.println("bits2 = HIGH");
      bit_2 = 4;
       }
       else {
       bit_2 = 0;
        //Serial.println("bits2 = LOW");
       }
       // bit3
       if (digitalRead(bits3) == HIGH){
       //Serial.println("bits3 = HIGH");
        bit_3 = 8;
       }
       else {
       bit_3 = 0;
       //Serial.println("bits3 = LOW");
      }

 // Adding up signals from UR-robot and printing them to the serial monitor
 Task_new = bit_0 + bit_1 + bit_2 + bit_3;
  Serial.print("Task_new = ");
  Serial.println(Task_new);

// Confirm legitimacy of signal
if (Task_new == Task_old){                      // Compare new signal with the last signal that diden't match the previus compleated Task
  Task = Task_new;                              // When a signal have already gone through once, and it repeats, the Task is chanced and compleated
}

if (Task_new != Task) {                         // Compare new signal with the previus compleated Task
  Task_old = Task_new;                          // When the new signal dosen't match the previus compleated Task, we store the new signal and check if it gets repeated
  delay(20);
}


// End of Task searching loop part, -> led flashes.
// led blinking to confirm loop running and arduino waiting for next task.
  digitalWrite(ledPin, HIGH);
  delay(100);
  digitalWrite(ledPin, LOW);
  delay(100);

// Ensures the same program dosen't run continuously
if (Task != LastRun){

// Printing which program will run to serial monitor
 Serial.print("Task Executing = ");
 Serial.println(Task);
 
 // Tool_1 = SuctionTool cover Tasks 1-9
// ShakerTable cover Tasks 10-15

// Task 0 = waiting for task
if (Task == 0) {                                // Checks if the task to be performed is task 0
   Serial.println("Waiting for task");
   LastRun = 0;                                 // Defines last run of current task
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // and thereby whaiting for the next task.
}

//Task 1 - Tool1 - Drives the piston back until limitswitch is reached
if (Task == 1) {
  LastRun = 1;
  digitalWrite(enablePin_T, LOW);               // Setting enablepin ready for motor control
  digitalWrite(dirPin_T, HIGH);                 // Setting dirpin ready for motor control
  Switchvardi_T = 0;                            // Resetting value from Max_out switch
  while (Switchvardi_T == 0){                   // Drives the piston back until Max_out is detected in one step increments
        digitalWrite(stepPin_T, HIGH);
        delayMicroseconds(700);
        digitalWrite(stepPin_T, LOW);
        delayMicroseconds(700);
        if (digitalRead(max_out) == LOW){
           Switchvardi_T = 0;
        }
        else{
             if (digitalRead(max_out) == HIGH){
                Switchvardi_T = 1;
             }
        }
  }
  digitalWrite(dirPin_T, LOW);                  // Resets motor pins
  digitalWrite(stepPin_T, LOW);                 // Resets motor pins
  digitalWrite(enablePin_T, HIGH);              // Resets motor pins
  digitalWrite(done, HIGH);                     // Sends command to UR-robot that the Arduino is done with current task
  delay(50);                                    // Waits 50ms
  stepper_T.setCurrentPosition(0);              // Sets the current position to be the new zero position
}

// Task 2 - Tool1 - Drives the piston forwards to the ready position 
if (Task == 2) {                                // Checks if the task to be performed is task 5
   LastRun = 2;                                 // Defines last run af current task
   RunStepper_T(1000,1000,-600);                // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
   stepper_T.setCurrentPosition(0);             // Sets the current position to be the new zero position
}

// Task 3 - Tool1 - Drives the piston to the zero position
if (Task == 3) {                                // Checks if the task to be performed is task 3
   LastRun = 3;                                 // Defines last run af current task
   RunStepper_T(10,200,0);                    // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 4 - Tool1 - Drives the piston to position 50 in relation to the zero position
if (Task == 4) {                                // Checks if the task to be performed is task 4
   LastRun = 4;                                 // Defines last run af current task
   RunStepper_T(1000,800,50);                   // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 5 - Tool1 - Drives the piston to position 60 in relation to the zero position
if (Task == 5) {                                // Checks if the task to be performed is task 5
   LastRun = 5;                                 // Defines last run af current task
   RunStepper_T(200,200,60);                   // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 6 - Tool1 - Drives the piston to position 70 in relation to the zero position
if (Task == 6) {                                // Checks if the task to be performed is task 6
   LastRun = 6;                                 // Defines last run af current task
   RunStepper_T(200,200,70);                   // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 7 - Tool1 - Drives the piston to position 80 in relation to the zero position
if (Task == 7) {                                // Checks if the task to be performed is task 7
   LastRun = 7;                                 // Defines last run af current task
   RunStepper_T(200,200,80);                  // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 8 - Tool1 - Drives the piston to position 120 in relation to the zero position
if (Task == 8) {                                // Checks if the task to be performed is task 8
   LastRun = 8;                                 // Defines last run af current task
   RunStepper_T(200,200,90);                  // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 9 - Tool1 - Drives the piston to position 250 in relation to the zero position
if (Task == 9) {                                // Checks if the task to be performed is task 9
   LastRun = 9;                                 // Defines last run af current task
   RunStepper_T(500,500,250);                  // Runs stepper as specified (speed,acceleration,position)
   digitalWrite(done, HIGH);                    // Sends command to UR-robot that the Arduino is done with current task
   delay(50);                                   // Waits 50ms
}

// Task 10 - Drives Shakertable - 4 rotations at 2 rotations pr. s
if (Task == 10) {                               // Checks if the task to be performed is task 10
   LastRun = 10;                                // Defines last run as current task
   RunStepper_S(3200,2000,6400);                // Runs stepper as specified (speed,acceleration,position)
   stepper_S.setCurrentPosition(0);             // Sets the shaker table position to 0, this is done to allow 
                                                // the shaker table to run continusly for a specified distance 
                                                // insted of moving to a given position
   delay(100);                                  // Waits 100ms
}

// Task 11 - Drives Shakertable - 4 rotations at 4.4 rotations pr. s
if (Task == 11) {                               // Checks if the task to be performed is task 11
   LastRun = 11;                                // Defines last run as current task
   RunStepper_S(7000,4000,6400);                // Runs stepper as specified (speed,acceleration,position)
   stepper_S.setCurrentPosition(0);             // Sets the shaker table position to 0, this is done to allow 
                                                // the shaker table to run continusly for a specified distance 
                                                // insted of moving to a given position
   delay(100);                                  // Waits 100ms
}

// Task 12 - Drives Shakertable - 5 rotations at 0.5 rotations pr. s
// UR-task: 3 - good at collection small objects in the middle of the tray
if (Task == 12) {                               // Checks if the task to be performed is task 12
   LastRun = 12;                                // Defines last run as current task
   RunStepper_S(800,4000,8000);                 // Runs stepper as specified (speed,acceleration,position)
   stepper_S.setCurrentPosition(0);             // Sets the shaker table position to 0, this is done to allow 
                                                // the shaker table to run continusly for a specified distance 
                                                // insted of moving to a given position
   delay(100);                                  // Waits 100ms
}

// Task 13 - Drives Shakertable - 1 rotations at 1 rotations pr. s repeated 10 times
// UR-task: 4
if (Task == 13) {                               // Checks if the task to be performed is task 13
  LastRun = 13;                                 // Defines last run as current task
  for (int i=0; i < 10; i++)                    // Loops 1 rotations at 1 rotations pr. s repeated 10 times
  {
   RunStepper_S(1600,10000,1600);               // Runs stepper as specified (speed,acceleration,position)
   stepper_S.setCurrentPosition(0);             // Sets the shaker table position to 0, this is done to allow 
                                                // the shaker table to run continusly for a specified distance
                                                // insted of moving to a given position 
   delay(100);                                  // Waits 100ms
  }
   delay(100);                                  // Waits 100ms
}


// Task 14 - Drives Shakertable - 6.25 rotations at 1 rotations pr. s
// UR-task: 5
if (Task == 14) {                               // Checks if the task to be performed is task 14
   LastRun = 14;                                // Defines last run as current task
   RunStepper_S(1600,4000,10000);               // Runs stepper as specified (speed,acceleration,position)
   stepper_S.setCurrentPosition(0);             // Sets the shaker table position to 0, this is done to allow 
                                                // the shaker table to run continusly for a spefifyed amount of time
                                                // insted of moving to a given position
   delay(100);                                  // Waits 100ms
}


// Task 15  - Drives Shakertable until photo position is reached
// UR-task: 2 (locked)
if (Task == 15) {                               // Checks if the task to be performed is task 15
   LastRun = 15;                                // Defines last run af current task
   digitalWrite(enablePin_S, LOW);              // Setting pins ready for motor control 
   digitalWrite(dirPin_S, HIGH);                // Setting pins ready for motor control
   Switchvardi_S = 0;                           // Resets Driving variables
   cnt_S = 0 ;                                  // Resets Driving variables
while (Switchvardi_S != 3){                     // Drives the motor until the reed_sensor has activated 3 times in a row,
                                                // this ensures no fails readings, produced by the magnetic fields from the motor.
    while (cnt_S < 3) {                         // If the table has been stopped inside the Reed_sensor zone, it will run a secount round to check.
      cnt_S = cnt_S + 1 ;
      digitalWrite(stepPin_S, HIGH);
      delayMicroseconds(650);
      digitalWrite(stepPin_S, LOW);
      delayMicroseconds(650);
      if (Switchvardi_S == 2) {                 // If two positive values are detected within the first 3 steps, 
          while (cnt_S < 800){                  // it is presumed that the position is inside the reed_sensor field,
            cnt_S = cnt_S + 1 ;                 // and the motor therefor will take an aditional half turn,
            digitalWrite(stepPin_S, HIGH);      // before finding the correct position.
            delayMicroseconds(650);
            digitalWrite(stepPin_S, LOW);
            delayMicroseconds(650);
          }
          Switchvardi_S = 0;                 
       }
        if (digitalRead(Reed_Switch) == LOW){
            Switchvardi_S = 0;
        }
        else{
             if (digitalRead(Reed_Switch) == HIGH){
                 Switchvardi_S = Switchvardi_S + 1;
             }
        }
    }
    digitalWrite(stepPin_S, HIGH);              // Stepping.
    delayMicroseconds(650);
    digitalWrite(stepPin_S, LOW);
    delayMicroseconds(650);
    if (digitalRead(Reed_Switch) == LOW){
            Switchvardi_S = 0;
    }
    else{
         if (digitalRead(Reed_Switch) == HIGH){
             Switchvardi_S = Switchvardi_S + 1;
         }
    }
}
  digitalWrite(dirPin_S, LOW);
  digitalWrite(stepPin_S, LOW);
  digitalWrite(enablePin_S, HIGH);
  digitalWrite(done, HIGH);                     // Sends command to UR-robot that the Arduino is done with current task
                                                // and thereby whaiting for the next task.
  delay(50);                                    // Waits 50ms
  stepper_S.setCurrentPosition(0);              // Sets the current step to pos. 0.
}
   

Serial.print("LastRun = ");                     //Prints the last run program in the serial monitor if posible
Serial.println(LastRun);                   

} // Closes "Task last run" if statement
} // Closes main loop

//----------------------------------------------------------------------------------------------------//

// Defines special function "RunStepper_S" for Tool 1
void RunStepper_T(int Speed, int Acceleration, int Steps)
{
  stepper_T.setMaxSpeed(Speed);                 // Sets max speed for the stepper motor (defined in steps per second) - this may be limited by the frequency of the microprocessor
  stepper_T.setAcceleration(Acceleration);      // Sets acceleration for the stepper motor (defined in steps per second^2)
  digitalWrite(enablePin_T, LOW);               // Sets enablepin low which "unlocks" the motor"
  stepper_T.moveTo(Steps);                      // Tells the steppermotor it's target position
  stepper_T.runToPosition();                    // Starts the motor
  digitalWrite(enablePin_T, HIGH);              // Sets enablepin high which "locks" the motor"
}

// Defines special function "RunStepper_T" for the shakertable
void RunStepper_S(int Speed, int Acceleration, int Steps)
{
  stepper_S.setMaxSpeed(Speed);                 // Sets max speed for the stepper motor (defined in steps per second) - this may be limited by the frequency of the microprocessor
  stepper_S.setAcceleration(Acceleration);      // Sets acceleration for the stepper motor (defined in steps per second^2)
  digitalWrite(enablePin_S, LOW);               // Sets enablepin low which "unlocks" the motor"
  stepper_S.moveTo(Steps);                      // Tells the steppermotor it's target position
  stepper_S.runToPosition();                    // Starts the motor
  digitalWrite(enablePin_S, HIGH);              // Sets enablepin high which "locks" the motor"
}
