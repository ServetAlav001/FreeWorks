int pinler[]={2,3,4,6,7,8,9};
int numaralar[10][7]={
  	{0,0,0,1,0,0,0},//sıfır
    {0,1,1,1,1,1,0},//bir
    {1,0,0,0,1,0,0},//iki
    {0,0,1,0,1,0,0},//uc
    {0,1,1,0,0,1,0},//dort
    {0,0,1,0,0,0,1},//bes
    {0,0,0,0,0,1,1},//altı
    {0,1,1,1,1,0,0},//yedi
    {0,0,0,0,0,0,0},//sekiz
    {0,0,1,0,0,0,0},//dokuz
};
void setup() {
  for(int i=0;i<7;i++){
  	pinMode(pinler[i],OUTPUT);
    digitalWrite(pinler[i],0);
  }
  pinMode(10,OUTPUT);
}
void loop() {
  for(int i=0;i<10;i++){
    for(int j=0;j<7;j++){
    	digitalWrite(pinler[j],numaralar[i][j]);
    }
    delay(1000);
    if(i==9){
    	digitalWrite(10,HIGH);
      	delay(2000);
      	digitalWrite(10,LOW);
    }
  }
  
}
