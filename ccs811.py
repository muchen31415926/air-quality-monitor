import time
import board
import adafruit_ccs811

i2c = board.I2C() 
ccs811 = adafruit_ccs811.CCS811(i2c)

# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass

while True:
    print(f"CO2: {ccs811.eco2} PPM, TVOC: {ccs811.tvoc} PPB")
    time.sleep(0.5)
