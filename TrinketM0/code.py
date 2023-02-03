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

# We need to first approximate the rise and fall
# for a single "bump" as the encoder would send
# as you turn it. The increment should be a turn
# clockwise (to raise intensity) while decrement
# is a counterclockwise turn.

def increment(sleepFor):
    # Rise
    time.sleep(sleepFor)
    p2.value = True
    time.sleep(sleepFor / 2)
    p1.value = True
    # Fall
    time.sleep(sleepFor)
    p2.value = False
    time.sleep(sleepFor / 2)
    p1.value = False

def decrement(sleepFor):
    # Rise
    time.sleep(sleepFor)
    p1.value = True
    time.sleep(sleepFor / 2)
    p2.value = True
    # Fall
    time.sleep(sleepFor)
    p1.value = False
    time.sleep(sleepFor / 2)
    p2.value = False

while True:
    # Just loop forever...

    if feedback:
        led[0] = (0, 255, 0) # Green for waiting
    time.sleep(5)

    if feedback:
        led[0] = (255, 0, 0) # Red for increase
    # It takes at least 3 "bumps" to register as an increase
    increment(0.06)
    increment(0.06)
    increment(0.06)
    time.sleep(2.0)

    if feedback:
        led[0] = (0, 0, 255) # Blue for decrease
    # It takes at least 3 "bumps" to register as a decrease
    decrement(0.06)
    decrement(0.06)
    decrement(0.06)
    time.sleep(2.0)
