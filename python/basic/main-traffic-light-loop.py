from gpiozero import *
from time import sleep
red = LED(22)
amber = LED(27)
green = LED(17)

def trafic_lights_loop():
    green.off()
    sleep(0.5)
    amber.on()
    sleep(0.5)
    amber.off()
    red.on()
    sleep(30)
    amber.on()
    sleep(2)
    red.off()
    amber.off()
    green.on()





loop = False

while loop == False:
    loop = input("Press enter to start traffic lights loop")
    loop = True

    while loop == True:
        trafic_lights_loop()
        loop = False

