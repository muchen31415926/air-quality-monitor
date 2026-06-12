from serial import Serial
from sds011lib import SDS011QueryReader
import time

PORT = 'COM5'

sensor = SDS011QueryReader(PORT)

while True:
    aqi = sensor.query()
    print('PM 2.5=',aqi.pm25)
    print('PM 10=',aqi.pm10)
    time.sleep(1)
