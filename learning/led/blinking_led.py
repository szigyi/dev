#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys

if len(sys.argv) == 2:
	pin=int(sys.argv[1])
	#pin=18

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

	try:
		GPIO.output(pin, GPIO.HIGH)
		sleep(1)
		GPIO.output(pin, GPIO.LOW)
		sleep(1)
		GPIO.output(pin, GPIO.HIGH)
		sleep(1)
		GPIO.output(pin, GPIO.LOW)
	except KeyboardInterrupt:
		GPIO.cleanup()
	finally:
		GPIO.cleanup()

else:
	print("You should provide a pin number (BCM) as an argument!")
