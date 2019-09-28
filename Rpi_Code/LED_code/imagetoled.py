#from PIL import Image
import os
import board
import busio
import digitalio
import adafruit_tlc5947
import time

'''
This program requires an image colormap.jpg to be put on the desktop of the pi. Creating this image involves:
    MS paint (or any other tool)
    resize the canvas to a ratio of imageheight : imagewidth
    paint in pure red or blue (255, 0, 0 or 0, 0, 255)
    ctrl A, reduce canvas size to imageheight * imagewidth
    save as colormap.jpg, transfer to pi via WinSCP
    
This program also assumes that a single chain of leds will be folded left and right multiple times to create a grid
https://www.adafruit.com/product/3635 is the LED strip this works with
'''


spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
latch = digitalio.DigitalInOut(board.D5)
tlc5947 = adafruit_tlc5947.TLC5947(spi, latch)

'''
imageheight=9
imagewidth=10

os.chdir("/")

colormap = Image.open('home/pi/Desktop/colormap.jpg')
r, g, b = colormap.split()
red=r.load() # indexes from top left as origin, +y down, +x right, [x, y]


x=0
y=0
counter=0

'''

for led in tlc5947:
    led=0
    #led.write()

for led in tlc5947:
    led=4095
    #led.write()
    time.sleep(1)
    led=0
    #led.write()

'''
while y<imageheight:
    while x<imagewidth:
        led=red[x,y]
        x=x+1*(-1)**y
        counter=counter+1
    x=x-1*(-1)**y
    y=y+1
'''