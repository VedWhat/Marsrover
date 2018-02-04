
import smbus

bus = smbus.SMBus(1)

address = 0x04

while True:
    a= int(input())
    
    pas=a%256 	
    bus.write_byte(0x04,pas)

    b=int(a/256)
    bus.write_byte(0x04,b)

    
    
	
