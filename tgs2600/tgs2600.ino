int gasSensor = 2; // 指定要量測的analog腳位為2
int gasval = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  gasval = analogRead(gasSensor);
  Serial.println( gasval );
  delay(500);
}