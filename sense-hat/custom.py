from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_rotation(180)
sense.low_light = True
sense.clear()

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # Black

def show():
    mx = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, X, O, O, O, O, O,
    X, O, X, O, O, O, O, O,
    X, X, O, O, O, O, O, O
    ]
    sense.set_pixels(mx)
    sleep(1)


# try:
#     while True:
#         show()
# except KeyboardInterrupt:
#     sense.show_message("Bye!")
# except Exception as e:
#     sense.clear()
#     print("Error {0}".format(str(e)).encode("utf-8"))

show()
exit()

