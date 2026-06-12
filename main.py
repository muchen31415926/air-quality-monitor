import time
from datetime import datetime

import serial
from sds011lib import SDS011QueryReader
import board
import adafruit_ccs811

# sds011
ser_sds011 = SDS011QueryReader('/dev/ttyUSB0')

# tgs2600
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

# ccs811
i2c = board.I2C()
ccs811 = adafruit_ccs811.CCS811(i2c)

while True:
    # sds011
    ts = datetime.now()
    aqi = ser_sds011.query()

    # tgs2600
    sensor_data = arduino.readline().decode('utf-8').strip()

    # ccs811
    print('{} PPM, TVOC-CCS={}, TGS-TVOC={} PPB, CO2={}, PM 2.5={}, PM 10={}'.format(
        ts, ccs811.tvoc, sensor_data, ccs811.eco2, aqi.pm25, aqi.pm10
    ))
    time.sleep(0.5)
