import smbus

bus=smbus.SMBus(1)

while(1):
    val=bus.read_byte(0x04)
    print(val)
