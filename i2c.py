import smbus
import time

device_address =  0x23
one_time_high_res_mode = 0x20

bus = smbus.SMBus(1)

def lightvalue():
    light = bus.read_i2c_block_data(device_address, one_time_high_res_mode)
    return Convert_val(light)

def Convert_val(data):
    return ((data[1] + (256 * data[0]))/ 1.2)

while True:
     Intensity = lightvalue()
     time.sleep(1)
     if(Intensity > 2500):
         print("Too Bright")
     elif(Intensity > 1500 and Intensity < 2500):
         print("Bright")
     elif(Intensity > 1000 and Intensity < 1500):
         print("Medium")
     elif(Intensity > 500 and Intensity < 1000):
         print("Dark")
     elif(Intensity < 500):
         print("Too Dark")
