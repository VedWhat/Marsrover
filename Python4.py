import smbus

bus=smbus.SMBus(1)

add=0x40

while True:
	a=int(input())
	
	p=a%256
 	bus.write_byte(0x04,p)

	b=int(a/256)
	bus.write_byte(0x04,b)

