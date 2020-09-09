
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def draw_whale(x,shape_width,padding=2):
    x=x+shape_width/4
    top = padding+10
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    # x = padding+40
    # Draw an ellipse.
    draw.ellipse((x, top, x+shape_width, bottom), outline=255, fill=0)
    # Draw a rectangle.
    #draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
    #x += shape_width+padding
    # Draw a triangle.
    belly = (bottom-top)
    center = top + belly/2
    fin = x-shape_width/4
    draw.polygon([(x,center) , (fin, center-belly/4), (fin, center+belly/4)], outline=255, fill=0)

    water = (x+shape_width/2)
    draw.polygon([(water, top+belly/8), (water-shape_width/16, padding), (water+shape_width/16, padding)], outline=255, fill=1)

    face = (x+shape_width-shape_width/4)
    eye = (x+shape_width-shape_width/8)
    # Draw an X.
    draw.line((face, top+belly/2, eye, top+belly/3), fill=255)
    draw.line((face, top+belly/3, eye, top+belly/2), fill=255)
    return

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
width = disp.width
height = disp.height

# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()

whale_width=30
x=-whale_width
while True:
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (width, height))
# Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
# Draw the beauty
    draw_whale(x,whale_width)
    draw_whale(x-50,whale_width-10)
    draw_whale(x-100,whale_width-20)
# Display image.
    disp.image(image)
    disp.display()
    x+=1
    time.sleep(.0)
    if x-100 >width: x=-whale_width

print("finish")
