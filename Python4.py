import time
import smbus

bus=smbus.SMBus(1)

add=0x40

def write(add,val):
	bus.write_byte(add,val)
	return -1

def read(add):
	num=bus.read_byte(add)
	return num

x=input("Input a val")
write(add,val)
time.sleep(1)

print(read(add)) 

