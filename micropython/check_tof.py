# Bernardo Giovanni (@cyb3rn0id)
# Code for testing the Time-Of-Flight Sensor ST VL53L7Cx

from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys

alvik = ArduinoAlvik()
alvik.begin()
alvik.set_illuminator(False) # turn off the color sensor illuminator

while True:
  
  l,lc,c,rc,r = alvik.get_distance() # front distance (left, left-center, center, right-center, right)
  t = alvik.get_distance_top() # top distance
  b = alvik.get_distance_bottom() # bottom distance
  
  print(f"top: {t} left:{l} center-left:{lc} center:{c} center-right:{rc} right:{r} bottom:{b}")
  sleep_ms(100)