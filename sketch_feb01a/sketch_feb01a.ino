
#include <Wire.h>

#define SLAVE_ADDRESS 0x04



void setup() {
  
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
 
  Wire.onReceive(receiveData);

}
int t=1;
int cnt=0;
int b=0;
int pas=0;

void loop() {
  delay(100);
} 

void receiveData(int c) {
  if(t==1)
  {
    pas= Wire.read();
    t=0;
    cnt = cnt + 1;
  }
  else if(t==0)
  {
     b = Wire.read();
    t=1;
    cnt = cnt + 1;
  }
  
  if (cnt == 2)
  {
     int aa= 256 * b + pas;
     cnt=0;
     Serial.println(aa);
  }
  
}  



