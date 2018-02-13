import smbus
import time


LSM9DS0_GYRO_ADDRESS    = 0x6B
#Gyro
LSM9DS0_WHO_AM_I_G      = 0x0F
LSM9DS0_CTRL_REG1_G     = 0x20
LSM9DS0_CTRL_REG3_G     = 0x22
LSM9DS0_CTRL_REG4_G     = 0x23
LSM9DS0_OUT_X_L_G       = 0x28
LSM9DS0_OUT_X_H_G       = 0x29
LSM9DS0_OUT_Y_L_G       = 0x2A
LSM9DS0_OUT_Y_H_G       = 0x2B
LSM9DS0_OUT_Z_L_G       = 0x2C
LSM9DS0_OUT_Z_H_G       = 0x2D

class LSM9DS0(object):
     # Gyro initialisation
        self.gyro.write8(LSM9DS0_CTRL_REG1_G, 0b00001111) # Normal power mode, XYZ enabled
        self.gyro.write8(LSM9DS0_CTRL_REG4_G, 0b00110000) # Continuous update, 2000 dps
      def readLowHigh(self, i2c_device, lowhigh):
        """Returns signed integer value by reading the given sensor's low and high
        bytes.
        """
        # Unpack low high register pair
        (low, high) = lowhigh

        # Combine the low and high bytes to create new binary value
        # Note the initial 'reading' is postive, so must be converted
        reading = i2c_device.readU8(low) | i2c_device.readU8(high) << 8

        # Convert to negative value if necessary
        if reading > 32767:
            reading -= 65536

        return reading

<<<<<<< HEAD
    def readSensor(self, i2c_device, xyz_lh):
        """Returns (x, y, z) tuple from the given sensor's registers
        """
        xyz = (self.readLowHigh(i2c_device, xyz_lh[0]),  # Pass x lowhigh registers
               self.readLowHigh(i2c_device, xyz_lh[1]),  # Pass y
               self.readLowHigh(i2c_device, xyz_lh[2]))  # Pass z

        return xyz
    
    def readGyro(self):
        """Return gyroscope (x, y, z) tuple"""

        return self.readSensor(self.gyro, LSM9DS0_OUT_XYZ_LH_G)

x,y,z=xyz
print(x,y,z)
time.sleep(0.5)
	 
=======
while True:
	a=int(input())
	
	p=a%256
 	bus.write_byte(0x04,p)

	b=int(a/256)
	bus.write_byte(0x04,b)
>>>>>>> ea8fff97b916c97d14d6223ea7408763659578af

