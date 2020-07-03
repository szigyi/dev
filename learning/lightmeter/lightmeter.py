#!/usr/bin/python3

import RPi.GPIO as GPIO
from PiAnalog import *
import time, datetime, math
from influxdb import InfluxDBClient

influx_client = InfluxDBClient("127.0.0.1", 8086, "grafana", "6153", "pi")

p = PiAnalog(C=0.33, R1=100.0)

def light_from_r(R):
	return math.log(1000000.0/R) * 10.0

def measure():
	measurement = p.read_resistance()
	# print(str(measurement))
	light = light_from_r(measurement)
	print(str(light))
	time = datetime.datetime.utcnow()
	body = [
		{
			"measurement": "light",
			"time": time,
			"fields": {
				"light": light
			}
		}
	]
	influx_client.write_points(body)


try:
	while True:
		measure()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
