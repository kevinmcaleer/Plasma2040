import plasma
from plasma import plasma2040
from time import sleep

NUM_LEDS = 150
FPS = 60

led_strip = plasma.APA102(NUM_LEDS, 0, 0, plasma2040.DAT, plasma2040.CLK)
led_strip.start(FPS)

# Light the first pixel Red
led_strip.set_rgb(0,128,128,128)