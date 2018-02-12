import smbus
import time
bus=smbus.SMBus(1)


while True:
	b=bus.read_byte(0x6b)
	print(b)
	time.sleep(1)


