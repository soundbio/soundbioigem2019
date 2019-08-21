from PIL import Image
import os
import board
import neopixel

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

imageheight=9
imagewidth=10

pixpin=board.D10

pixnum=imageheight*imagewidth

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixpin, pixnum)

os.chdir("/")

colormap = Image.open('home/pi/Desktop/colormap.jpg')
r, g, b = colormap.split()
red=r.load() # indexes from top left as origin, +y down, +x right, [x, y]
blue=b.load()

x=0
y=0
counter=0

pixels.fill((0, 0, 0))

while y<imageheight:
    while x<imagewidth:
        pixels[counter]=(red[x, y], 0, blue[x, y])
        x=x+1*(-1)**y
        counter=counter+1
    x=x-1*(-1)**y
    y=y+1