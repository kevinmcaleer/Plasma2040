# Race a single pixel
import plasma
from plasma import plasma2040
from time import sleep

NUM_LEDS = 150
FPS = 60

led_strip = plasma.APA102(NUM_LEDS, 0, 0, plasma2040.DAT, plasma2040.CLK)
led_strip.start(FPS)
while True:
    
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i,128,0,0)
        if i > 0:
            led_strip.set_rgb(i-1,0,0,0)
        
        sleep(0.01)
