import time
import smbus

bus=smbus.SMBus(1)

add=0x40

while True:
	a=int(input())
	bus.write_byte(add,a)



