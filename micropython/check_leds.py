# Bernardo Giovanni (@cyb3rn0id)
# Code for testing the Leds on Arduino Alvik Carrier Board and Leds on Arduino Nano ESP32

from arduino_alvik import ArduinoAlvik
from time import sleep_ms
from machine import Pin # this is for controlling individual Arduino Nano ESP32 pins
import sys

alvik = ArduinoAlvik()
alvik.begin()
alvik.set_illuminator(False) # turn off the color sensor illuminator

# we have 3 leds on alvik carrier board, driven by the STM32
# builtin_led => this is the orange led on the back of the robot, near the left QWIIC connector
# DL1 or left_led => the RGB led on top-left
# DL2 or right_led => the RGB led on top-right
# you can set RGB led colors using the set_color(R,G,B) method, where R,G,B can be 0 or 1

# the Arduino Nano ESP32 itself has his own 2 leds
# led_builtin (on GPIO48) => orange led on the left of the USB connector
# an RGB led on the right of the reset button (Red=GPIO46, Green=GPIO0, Blue=GPIO45)
# NOTE: the Arduino RGB leds will turn ON when you drive the pin LOW (so, for turning it on, you must write 'off()')
# since is not so intuitive writing 'on' for turning 'off' a led, I wrote my own function

# Arduino Nano ESP32 leds
LED = Pin('LED_BUILTIN', Pin.OUT) # orange led
LEDR = Pin(46, Pin.OUT)
LEDG = Pin(0, Pin.OUT)
LEDB = Pin(45, Pin.OUT)

# my own function for using the Arduino Nano ESP32 RGB led
def nanoesp32_set_rgb_led(r:int, g:int, b:int):
  
  if r==0:
    LEDR.on()
  else:
    LEDR.off()
  
  if g==0:
    LEDG.on()
  else:
    LEDG.off()
  
  if b==0:
    LEDB.on()
  else:
    LEDB.off()


while True:

  # Arduino Nano ESP32 own leds
  LED.on() # orange led ON
  
  # RGB led using my own function
  nanoesp32_set_rgb_led(1,0,0)
  sleep_ms(500)
  nanoesp32_set_rgb_led(0,1,0)
  sleep_ms(500)
  nanoesp32_set_rgb_led(0,0,1)
  sleep_ms(500)

  # Arduino Nano ESP32, leds off
  nanoesp32_set_rgb_led(0,0,0)
  LED.off()
  
  # Alvik Carrier board builtin_led
  alvik.set_builtin_led(True)
  sleep_ms(1000)
  alvik.set_builtin_led(False)

  # left led red - right led off
  alvik.DL1.set_color(1,0,0)
  alvik.DL2.set_color(0,0,0)
  sleep_ms(1000)

  # left led off - right led red
  alvik.DL1.set_color(0,0,0)
  alvik.DL2.set_color(1,0,0)
  sleep_ms(1000)

  # left led green - right led off
  alvik.DL1.set_color(0,1,0)
  alvik.DL2.set_color(0,0,0)
  sleep_ms(1000)

  # left led off - right led green
  alvik.DL1.set_color(0,0,0)
  alvik.DL2.set_color(0,1,0)
  sleep_ms(1000)

  # left led blue - right led off
  alvik.DL1.set_color(0,0,1)
  alvik.DL2.set_color(0,0,0)
  sleep_ms(1000)

  # left led off - right led blue
  alvik.DL1.set_color(0,0,0)
  alvik.DL2.set_color(0,0,1)
  sleep_ms(1000)
  alvik.DL2.set_color(0,0,0)