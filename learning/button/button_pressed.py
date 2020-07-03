#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

pin=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(pin) == GPIO.HIGH:
			print("Pin " + str(pin) + " is 1/GPIO.HIGH/True - button pressed")
		else:
			print("Pin " + str(pin) + " is 0/GPIO.LOW/False - button not pressed")
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
