from sense_hat import SenseHat
from time import sleep
from Graph import Graph
import GraphUtil
from State import StateManager, State

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
    sleep(4)


temperature_state = State(temperature)
humidity_state = State(humidity)
graph_state = State(graph)
state_manager = StateManager([graph_state, temperature_state, humidity_state])


try:
    while True:
        state_manager.next()
except KeyboardInterrupt:
    sense.show_message("Bye!")
except Exception as e:
    sense.clear()
    print("Error {0}".format(str(e.args[0])).encode("utf-8"))

exit()

   
   