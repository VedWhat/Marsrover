import smbus
<<<<<<< HEAD
import time
bus=smbus.SMBus(1)


while True:
	b=bus.read_byte(0x6b)
	print(b)
	time.sleep(1)


=======

bus=smbus.SMBus(1)

while(1):
    val=bus.read_byte(0x04)
    print(val)
>>>>>>> ea8fff97b916c97d14d6223ea7408763659578af
