#!usr/bin/env python3
from gpiozero import LED
from time import sleep
red = LED(22)
amber = LED(27)
green = LED(17)

red.on()
sleep(1)
amber.on()
sleep(1)
green.on()
sleep(1)