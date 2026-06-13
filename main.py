import time
from datetime import datetime

import serial
from sds011lib import SDS011QueryReader
import board
import adafruit_ccs811

from db_wrapper import DBWrapper

#db
db = DBWrapper()

# sds011
ser_sds011 = SDS011QueryReader('/dev/ttyUSB0')

# tgs2600
arduino = serial.Serial('/dev/ttyACM0', 9600)

# ccs811
i2c = board.I2C()
ccs811 = adafruit_ccs811.CCS811(i2c)

while True:
    # sds011
    ts = datetime.now()
    sds_data = ser_sds011.query()

    # tgs2600
    tgs_tvoc = arduino.readline().decode('utf-8').strip()

    # ccs811
    ccs_tvoc = ccs811.tvoc
    ccs_eco2 = ccs811.eco2
    
    #inser to db
    data = {
        'timestamp': ts,
        'ccs_tvoc': ccs_tvoc,
        'tgs_tvoc': tgs_tvoc,
        'eco2': ccs_eco2,
        'pm25': sds_data.pm25,
        'pm10': sds_data.pm10
    }

    db.insert_data(data)

    print('{} PPM, CCS-TVOC={}, TGS-TVOC={} PPB, ECO2={}, PM 2.5={}, PM 10={}'.format(
        ts, ccs_tvoc, tgs_tvoc, ccs_eco2, sds_data.pm25, sds_data.pm10
    ))

    time.sleep(1)
