#!/usr/bin/env python3

import time
import datetime
import psutil
from influxdb import InfluxDBClient
import RPi.GPIO as GPIO
from PiAnalog import *

# influx configuration - edit these
ifuser = "grafana"
ifpass = "6153"
ifdb   = "pi"
ifhost = "127.0.0.1"
ifport = 8086
measurement_name = "external_temperature"

# connect to influx
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

p = PiAnalog()

def measure():
    # take a timestamp for this measurement
    time = datetime.datetime.utcnow()

    temp = p.read_temp_c(3800, 1000)
    temp = "%.2f" % temp

    # format the data as a single measurement for influx
    body = [
        {
            "measurement": measurement_name,
            "time": time,
            "fields": {
                "external_temp": temp,
            }
        }
    ]

    # write the measurement
    ifclient.write_points(body)


try:
    while True:
        measure()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
finally:
    GPIO.cleanup()
    raise
