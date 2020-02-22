from guizero import App, Text, PushButton
from gpiozero import TrafficLights
from time import sleep
# Set the pins the traffic light uses on the raspberry pi
lights = TrafficLights(22, 27, 17)
#Defines The Function Which Declares What The Program Should do For the traffic light loop
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


#Sets app Title bar labelAnd sets the  layout type
app = App("Traffic Lights controller", layout="grid")
#Creates button grid for Individual red light controller
Text(app, "Red", grid=[0, 0])
PushButton(app, command=lights.red.on, text="on", grid=[1, 0])
PushButton(app, command=lights.red.off, text="off", grid=[2, 0])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 0])

Text(app, "Amber", grid=[0, 1])
#Creates button grid for Individual Amber light controller
PushButton(app, command=lights.amber.on, text="on", grid=[1,1])
PushButton(app, command=lights.amber.off,text="off", grid=[2, 1])
PushButton(app, command=lights.amber.blink, text="blink", grid=[3, 1])
#Creates button grid for Individual Green light controller
Text(app, "Green", grid=[0, 2])
PushButton(app, command=lights.green.on, text="on", grid=[1,2])
PushButton(app, command=lights.green.off, text="off", grid=[2,2])
PushButton(app, command=lights.green.blink, text="blink", grid=[3,2])
#Creates button grid for All light control
Text(app, "All", grid=[0,3])
sxxuence", grid=[2,4])
PushButton(app, command=trafic_
#Creates button And label grid For the clear traffic light sequence functions
Text("reset lights", grid=[3,6])
PushButton(app, command=lights.off, text="clear lights", grid=[3,5])

#And finally sets The app to display on the screen
app.display()
