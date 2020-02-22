from guizero import App, Text, PushButton
from gpiozero import TrafficLights
from time import sleep
red = LED(22)
amber = LED(27)
green = LED(17)

lights = TrafficLights(22, 27, 17)
def trafic_lights_loop():
    lights.green.off()
    sleep(0.5)
    lights.amber.on()
    sleep(0.5)
    lights.amber.off()
    lights.red.on()
    sleep(0.5)
    lights.amber.on()
    sleep(2)
    lights.red.off()
    lights.amber.off()
    lights.green.on()

app = App("Traffic Lights controller", layout="grid")

Text(app, "Red", grid=[0, 0])
PushButton(app, command=lights.red.on, text="on", grid=[1, 0])
PushButton(app, command=lights.red.off, text="off", grid=[2, 0])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 0])


Text(app, "Amber", grid=[0, 1])
PushButton(app, command=lights.amber.on, text="on", grid=[1,1])
PushButton(app, command=lights.amber.off,text="off", grid=[2, 1])
PushButton(app, command=lights.amber.blink, text="blink", grid=[3, 1])

Text(app, "Green", grid=[0, 2])
PushButton(app, command=lights.green.on, text="on", grid=[1,2])
PushButton(app, command=lights.green.off, text="off", grid=[2,2])
PushButton(app, command=lights.green.blink, text="blink", grid=[3,2])

Text(app, "All", grid=[0,3])
PushButton(app, command=lights.on, text="on", grid=[1,3])
PushButton(app, command=lights.off, text="off", grid=[2,3])
PushButton(app, command=lights.blink, text="blink", grid=[3,3])

Text(app, "Traffic light sequence", grid=[2,4])
PushButton(app, command=trafic_lights_loop, text="run loop", grid=[2, 5])


app.display()