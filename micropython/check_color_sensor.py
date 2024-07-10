# Bernardo Giovanni (@cyb3rn0id)
# Code for testing the Color/Light sensor Broadcom ADPS-9960 

from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys

alvik = ArduinoAlvik()
alvik.begin()

# this will turn on the white leds near the sensor
# led will turn off if sensor is too far from objects
alvik.set_illuminator(True)

# I'll store in this string the previous-detected color
# so I can refresh the new detected color only if different than the previous one
precolor=""

# remember: if color are not correctly detected you can use the following instructions
# for re-calibrate the color sensor:
# alvik.color_calibration('white') # calibrate sensor with a perfectly white surface
# alvik.color_calibration('black') # calibrate sensor with a perfectly black surface

while True:
  
  h,s,v = alvik.get_color('hsv') # get color in Hue, Saturation, Value format
  color = alvik.hsv2label(h,s,v) # translate the H,S,V color in a label
  
  # if color is different than the previous one, write it in the repl
  if (color != precolor):
    print(alvik.hsv2label(h,s,v))
    precolor=color
  sleep_ms(100)