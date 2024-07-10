# Bernardo Giovanni (@cyb3rn0id)
# Code for testing the Line sensor

from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys

alvik = ArduinoAlvik()
alvik.begin()
alvik.set_illuminator(False) # turn off the color sensor illuminator

while True:
  
  # line detection works best if line is about 2cm wide 
  # black line on white background or white line on black background
  # smaller the number, more white is the detected surface
  # greated the number, more black is the detected surface
  
  l,c,r = alvik.get_line_sensors() # read values from sensors
  
  print(f"Left: {l} Center:{c} Right:{r}")
  sleep_ms(100)
