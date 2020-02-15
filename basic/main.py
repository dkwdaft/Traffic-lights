#!usr/bin/env ppython3
from gpiozero import LED
red = LED(22)
while True:
    red.blink()


