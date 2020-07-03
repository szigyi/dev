#!/usr/bin/python3

import RPi.GPIO as GPIO
from PiAnalog import *
import time

p = PiAnalog()

try:
	while True:
		temp = p.read_temp_c(3800, 1000)
		temp = "%.2f" % temp
		print(temp)
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
