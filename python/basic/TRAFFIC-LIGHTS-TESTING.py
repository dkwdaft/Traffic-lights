#!usr/bin/env python3
from gpiozero import LED
from time import sleep
red = LED(22)
amber = LED(27)
green = LED(17)
print("Calibrating traffic light and sleep function")
red.on()
sleep(1)
amber.on()
sleep(1)
green.on()
sleep(1)

green.off()
amber.off()
red.off()
sleep(1)
i = 1
print("turning the lights on and off in sequence once.")
red.on()
sleep(1)
amber.on()
sleep(1)
green.on()
sleep(1)
red.off()
sleep(1)
amber.off()
sleep(1)
green.off()
sleep(1)



