import board
import busio
import adafruit_tsl2591
import digitalio
import adafruit_tlc5947
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
latch = digitalio.DigitalInOut(board.D5)
tlc5947 = adafruit_tlc5947.TLC5947(spi, latch)

for led in tlc5947:
    led=0
    #led.write()

try:
    for led in tlc5947:
        led=4095
        #led.write()
        time.sleep(0.3)
        led=0
        #led.write()
        
    for led in tlc5947:
        led=4095
        #led.write()
    
    while True:
        print(sensor.lux)
        
except KeyboardInterrupt:
    for led in tlc5947:
        led=0
        #led.write
