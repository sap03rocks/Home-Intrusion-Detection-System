#include <Servo.h>

const int trigPin = 10;
const int echoPin = 11;

const int startSensorPin = 2;
const int stopSensorPin = 3;

const int buzzerPin = 4;
const int ledPin = 5;

bool isServoRunning = false;
int lastPosition = 15;

Servo myServo;

void setup() {
  pinMode(startSensorPin, INPUT);
  pinMode(stopSensorPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(9600);

  myServo.attach(12);
  myServo.write(lastPosition);

  Serial.println("Servo control initialized");
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    Serial.print("Received command: ");
    Serial.println(command);

    if (command.equals("yes")) {
      // Start the servo movement
      if (!isServoRunning) {
        isServoRunning = true;
        myServo.attach(12); // Reattach the servo
        myServo.write(lastPosition); // Set the initial position
        Serial.println("Servo movement started");
      }
    } else if (command.equals("no")) {
      // Stop the servo movement
      if (isServoRunning) {
        lastPosition = myServo.read();
        isServoRunning = false;
        myServo.detach(); // Stop sending control signals to the servo
        digitalWrite(buzzerPin, LOW); // Turn off the buzzer
        digitalWrite(ledPin, LOW); // Turn off the LED
        Serial.println("Servo movement stopped");
      }
    }
  }

  if (isServoRunning) {
    for (int i = lastPosition; i <= 165; i++) {
      myServo.write(i);
      delay(30);
      int distance = calculateDistance();
      Serial.print(i);
      Serial.print(",");
      Serial.print(distance);
      Serial.print(".");

      if (!isServoRunning) {
        break; // Stop the loop if servo is no longer running
      }

      if (distance <= 40 && distance >= 0) {
        int frequency = map(distance, 0, 40, 2000, 500); // Map distance to frequency range
        int duration = map(distance, 0, 40, 200, 20); // Map distance to duration range
        tone(buzzerPin, frequency, duration); // Generate tone on the buzzer
        digitalWrite(ledPin, HIGH); // Turn on the LED
      } else {
        noTone(buzzerPin); // Turn off the buzzer
        digitalWrite(ledPin, LOW); // Turn off the LED
      }
    }

    if (!isServoRunning) {
      // Skip the reverse loop if the servo has stopped
    } else {
      for (int i = 166; i >= lastPosition; i--) {
        myServo.write(i);
        delay(30);
        int distance = calculateDistance();
        Serial.print(i);
        Serial.print(",");
        Serial.print(distance);
        Serial.print(".");

        if (!isServoRunning) {
          break; // Stop the loop if servo is no longer running
        }

        if (distance <= 40 && distance >= 0) {
          int frequency = map(distance, 0, 40, 2000, 500); // Map distance to frequency range
          int duration = map(distance, 0, 40, 200, 20); // Map distance to duration range
          tone(buzzerPin, frequency, duration); // Generate tone on the buzzer
          digitalWrite(ledPin, HIGH); // Turn on the LED
        } else {
          noTone(buzzerPin); // Turn off the buzzer
          digitalWrite(ledPin, LOW); // Turn off the LED
        }
      }
    }
  }
}

int calculateDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;
  return distance;
}
