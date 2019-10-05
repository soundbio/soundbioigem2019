import board
import busio
import adafruit_tsl2591
import csv

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

with open('lux_values.csv', 'wb') as csvfile:
filewriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['LED', 'Distance', 'LuxValue'])

for led in range(48)

    luxValues = []
    distance = int(input())

    for i in range(1000):
        luxValues.append(sensor.lux)
        
    averageLux = sum(luxValues) / len(luxValues)

    with open('lux_values.csv', 'a') as csvfile:
        csvfile.writerow([ledName, distance, averageLux])


