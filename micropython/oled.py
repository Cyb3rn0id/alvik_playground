# Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys

alvik = ArduinoAlvik()
alvik.begin()

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

# SCL = Phisical pin 9 = ESP32 pin GPIO12 - Arduino Digital pin D22 / Analog Pin A5 
# SDA = Phisical pin 8 = ESP32 pin GPIO11 - Arduino Digital pin D21 / Analog Pin A4

i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display (width, height, i2c instance, default address=0x3C)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Add some text
oled.text("Arduino Nano",5,5)
oled.text("ESP32",5,15)

# Finally update the oled display so the image & text is displayed
oled.show()