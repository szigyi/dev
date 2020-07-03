#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin=25

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#raw_input("Press Enter when ready\n>")

try:
	GPIO.wait_for_edge(pin, GPIO.FALLING)
	print("Falling detected - button pressed")
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
