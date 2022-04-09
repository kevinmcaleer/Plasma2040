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
while True:
    for i in range(NUM_LEDS):
        offset += float(speed) / 2000.0
        hue = float(i) / NUM_LEDS
            
        led_strip.set_hsv(i, hue + offset, 1.0, 0.5)
        
        if direction == 1:
            if brightness == 31:
                direction = 0
            else:
                brightness += 1
        else:
            if brightness == 5:
                direction = 1
            else:
                brightness -= 1
        led_strip.set_brightness(brightness)
        print(f"hue: {hue}, i: {i}, brightness: {brightness}, saturation: {saturation}")
        sleep(0.01)
