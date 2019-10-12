import board
import busio
import adafruit_tsl2591
import csv

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

print(sensor.lux)

