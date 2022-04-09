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

HUE = 0.9
SATURATION = 1
BRIGHTNESS = 1
while True:
    for i in range(NUM_LEDS):
        led_strip.set_hsv(i, HUE, SATURATION, BRIGHTNESS)
#     led_strip.set_brightness(BRIGHTNESS)

