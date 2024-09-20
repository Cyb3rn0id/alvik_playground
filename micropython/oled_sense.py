from arduino_alvik import ArduinoAlvik
from time import sleep_ms
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import sys

alvik = ArduinoAlvik()
alvik.begin()

WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height
precolor=""


# SCL = Phisical pin 9 = ESP32 pin GPIO12 - Arduino Digital pin D22 / Analog Pin A5 
# SDA = Phisical pin 8 = ESP32 pin GPIO11 - Arduino Digital pin D21 / Analog Pin A4
i2c = I2C(0) # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display (width, height, i2c instance, default address=0x3C)

# Clear the oled display
oled.fill(0)
# Micropython logo
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)

oled.text('ALVIK DEMO', 40, 0, 1)
oled.text('@CYB3RN0ID', 40, 9, 1)
oled.text('PRESS   OK', 40, 18, 1)
oled.text('TO   START', 40, 27, 1)
oled.show()

alvik.left_led.set_color(0, 1, 0)
alvik.right_led.set_color(0, 1, 0)
alvik.set_illuminator(False)

while not alvik.get_touch_ok():
    sleep_ms(50)

oled.fill(0)
oled.show()
alvik.set_illuminator(True)

try:
    while True:
        while not alvik.get_touch_cancel():
            alvik.left_led.set_color(0, 0, 0)
            alvik.right_led.set_color(0, 0, 0)
            L, CL, C, CR, R = alvik.get_distance()
            h,s,v = alvik.get_color('hsv') # get color in Hue, Saturation, Value format
            color = alvik.hsv2label(h,s,v) # translate the H,S,V color in a label

           
            oled.fill(0)
            oled.text(alvik.hsv2label(h,s,v),0,0,1)
            oled.text(f'L:  {L}',0,9,1)
            oled.text(f'CL: {CL}',0,18,1)
            oled.text(f'C:  {C}',0,27,1)
            oled.text(f'CR: {CR}',0,36,1)
            oled.text(f'R:  {R}',0,44,1)
            oled.show()
            
            error = C - reference
            #alvik.set_wheels_speed(error*10, error*10)
            
            sleep_ms(100)

        while not alvik.get_touch_ok():
            alvik.left_led.set_color(0, 1, 0)
            alvik.right_led.set_color(0, 1, 0)
            oled.fill(0)
            oled.text('ALVIK STOPPED',0,0,1)
            oled.show()
            alvik.brake()
            sleep_ms(100)
          
except KeyboardInterrupt as e:
    print('over')
    alvik.stop()
    sys.exit()
