void setup() {
  // put your setup code here, to run once:
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() {
  digitalWrite(3, HIGH);
  delay(100);
  digitalWrite(3, LOW);
  delay(100);
  digitalWrite(5, HIGH);
  delay(100);
  digitalWrite(5, LOW);
  delay(100);
  digitalWrite(6, HIGH);
  delay(100);
  digitalWrite(6, LOW);
  delay(100);

}
