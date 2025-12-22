int irPin = 2;
int led = 8;

void setup() {
  pinMode(irPin, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int pot = analogRead(A0);        // 0–1023
  int ir = digitalRead(irPin);     // 0 veya 1

  Serial.print("Pot: ");
  Serial.print(pot);
  Serial.print("  IR: ");
  Serial.println(ir);

  if (ir == LOW && pot > 500) {    // pot ile şart ekledik
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }

  delay(100);
}
