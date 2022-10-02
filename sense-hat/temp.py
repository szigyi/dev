from sense_hat import SenseHat
from time import sleep
from Graph import Graph
import GraphUtil


sense = SenseHat()

sense.set_rotation(180)
sense.low_light = True
# sense.gamma = [1] * 32
sense.clear()

white = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

min_temp = 19
max_temp = 25
g = Graph(min_temp, max_temp)


def temperature():
    temp = sense.get_temperature()
    scaled_temp = GraphUtil.rescale(min_temp, max_temp, temp) - 1
    col = GraphUtil.temp_colour(scaled_temp, blue, green, red)
    sense.show_message(str(round(temp, 1)) + "C", 0.1, col)


def humidity():
    hum = sense.get_humidity()
    sense.show_message(str(round(hum, 1)) + "%", 0.1, white)


def graph():
    temp = sense.get_temperature()
    pixels = g.render(temp)
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

   
   