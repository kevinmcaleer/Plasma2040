# Pulse colours

import plasma
from plasma import plasma2040
from time import sleep

NUM_LEDS = 150
FPS = 60
SPEED = 0.0001

led_strip = plasma.APA102(NUM_LEDS, 0, 0, plasma2040.DAT, plasma2040.CLK)
led_strip.start(FPS)
while True:
    
    for l in range(0,255,10):
        for k in range(0,255,10):
            for j in range(100,255):
                for i in range(NUM_LEDS):
                    led_strip.set_rgb(i,j,k,l)    
                sleep(SPEED)
    #         sleep(0.25)   
            for j in range(255,100,-1):
                for i in range(NUM_LEDS):
                    led_strip.set_rgb(i,j,k,l)
                sleep(SPEED)
    #         sleep(0.25)
            print(k, l)
