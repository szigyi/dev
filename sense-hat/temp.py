from sense_hat import SenseHat
from time import sleep
from Graph import Graph



sense = SenseHat()

sense.set_rotation(180)
sense.low_light = True
sense.clear()

white = (200,200,200)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def temperature():
    temp = sense.get_temperature()
    col = blue
    if temp >= 24:
        col = red
    elif temp < 24 and temp >= 21:
        col = green
    sense.show_message(str(round(temp, 1)) + "C", 0.1, col)

def humidity():
    hum = sense.get_humidity()
    sense.show_message(str(round(hum, 1)) + "%", 0.1, white)

def graph():
    graph = Graph(14, 30)
    temp = sense.get_temperature()
    pixels = graph.render(temp)
    sense.set_pixels(pixels)


try:
    while True:
        graph()
        sleep(4)
        temperature()
        sleep(0.5)
        humidity()
except KeyboardInterrupt:
    sense.show_message("Bye!")
except Exception as e:
    sense.clear()
    print("Error {0}".format(str(e.args[0])).encode("utf-8"))

exit()

   
   