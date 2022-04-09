# Pulse colours

import plasma
from plasma import plasma2040
from time import sleep

NUM_LEDS = 150
FPS = 60
speed = 10

led_strip = plasma.APA102(NUM_LEDS, 0, 0, plasma2040.DAT, plasma2040.CLK)
led_strip.start(FPS)
offset = 1
direction = 1
brightness = 1
saturation = 1
sat_dir = 1

HUE = 0.1
SATURATION = 1
BRIGHTNESS = 0.5
while True:
    for h in range (1, 100, 1):
        for i in range(NUM_LEDS):
            led_strip.set_hsv(i, float(h)/100, SATURATION, BRIGHTNESS)
        sleep(0.0001)
#     led_strip.set_brightness(BRIGHTNESS)

