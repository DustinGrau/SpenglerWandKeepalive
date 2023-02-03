# Hasbro Spengler Neutrona Wand Keepalive
#
# Dustin Grau - dustin.grau@gmail.com
#  - Atlanta Ghostbusters -
#
# Released under the Apache 2.0 license
#
# Designed to work with the digital encoder (dial)
# in the Neutrona Wand to send a high (+VCC) signal
# to the encoder controls (wand intensity) via the
# A/B signal wires in order to cheat the built-in
# 30-second timeout.

import board
import random
import time
from digitalio import DigitalInOut, Direction

# Set a flag for visual feedback via the DotStar LED
feedback = True

# Use the built-in DotStar LED for feedback when in feedback mode
if feedback:
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
    led.brightness = 0.1

# Digital encoder pin 1 (using pin 3)
p1 = DigitalInOut(board.D3)
p1.direction = Direction.OUTPUT

# Digital encoder pin 2 (using pin 4)
p2 = DigitalInOut(board.D4)
p2.direction = Direction.OUTPUT

def increment(sleepFor):
    p2.value = True
    time.sleep(sleepFor)
    p1.value = True
    time.sleep(sleepFor)
    p2.value = False
    time.sleep(sleepFor)
    p1.value = False
    time.sleep(sleepFor)
    p2.value = False
    time.sleep(sleepFor)
    p1.value = False

def decrement(sleepFor):
    p1.value = True
    time.sleep(sleepFor)
    p2.value = True
    time.sleep(sleepFor)
    p1.value = False
    time.sleep(sleepFor)
    p2.value = False
    time.sleep(sleepFor)
    p1.value = False
    time.sleep(sleepFor)
    p2.value = False

while True:
    # Turn the LED green while in a waiting state
    if feedback:
        led[0] = (0, 255, 0)
    time.sleep(5)

    if feedback:
        led[0] = (255, 0, 0)
    increment(0.06)
    increment(0.06)
    increment(0.06)
    time.sleep(2.0)

    if feedback:
        led[0] = (0, 0, 255)
    decrement(0.06)
    decrement(0.06)
    decrement(0.06)
    time.sleep(2.0)
