from gpiozero import *
from time import sleep
red = LED(22)
amber = LED(27)
green = LED(17)

def trafic_lights_loop():
    green.on()
    sleep(0.5)
    green.off()
    sleep(0.5)
    amber.on()
    sleep(0.5)
    amber.off()
    sleep(0.5)
    red.on()
    sleep(0.5)
    amber.on()
    sleep(0.5)
    red.off()
    amber.off()
    sleep(0.5)
    green.on()




while loop == False:
    loop = input("Press enter to start traffic lights loop")
    if "quit" or "QUIT" in loop:
        quit()
    else:
        loop = True

    while loop == True:
        trafic_lights_loop()
        loop = False

