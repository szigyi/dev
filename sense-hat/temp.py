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

min_temp = 20
max_temp = 24
g = Graph(min_temp, max_temp)

def compensated_temperature():
    return sense.get_temperature() - 1


def temperature():
    temp = compensated_temperature()
    scaled_temp = GraphUtil.rescale(min_temp, max_temp, temp) - 1
    col = GraphUtil.temp_colour(scaled_temp, blue, green, red)
    sense.show_message(str(round(temp, 1)) + "C", 0.1, col)


def humidity():
    hum = sense.get_humidity()
    sense.show_message(str(round(hum, 1)) + "%", 0.1, white)


def graph():
    temp = compensated_temperature()
    pixels = g.render(temp)
    sense.set_pixels(pixels)
    sleep(10)


temperature_state = State(temperature)
humidity_state = State(humidity)
graph_state = State(graph)
state_manager = StateManager([graph_state, temperature_state, humidity_state])


loop_state = True
try:
    while True:
        for event in sense.stick.get_events():
            print("event", event)
            if event.action == "pressed":
                if event.direction == "middle":
                    loop_state = True  # reset to the normal screen cycle
                elif event.direction == "right":
                    loop_state = False
                    state_manager.next()

        if loop_state:
            state_manager.next()
        else:
            state_manager.refresh()
except KeyboardInterrupt:
    sense.show_message("Bye!")
except Exception as e:
    sense.clear()
    print("Error {0}".format(str(e.args[0])).encode("utf-8"))

exit()

   
   
   