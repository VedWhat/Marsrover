import smbus

bus=smbus.SMBus(1)

add=0x40

while True:
	a=input()
	v=list(a)
	for i in list:
		val=int(i)
		bus.write_byte(add,a)



