import serial
import time

arduino = serial.Serial('COM4', 9600)
time.sleep(2)

while True:
  sensor_data = arduino.readline().decode('utf-8').strip()
  print(f"TGS-TVOC: {sensor_data}")
  time.sleep(1)