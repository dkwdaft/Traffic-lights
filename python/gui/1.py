from guizero import App, Text, PushButton
from gpiozero import TrafficLights

lights = TrafficLights(22, 27, 17)


app = App()


PushButton(app, command=lights.red.on, text="on")

app.display()