#!usr/bin/env ppython3
from gpiozero import LED
from  time import sleep
red = LED(22)
while True:
    red.blink()
    sleep(5)


