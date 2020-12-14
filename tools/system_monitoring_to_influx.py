#!/usr/bin/env python

import time
import datetime
import psutil
from influxdb import InfluxDBClient

# influx configuration - edit these
ifuser = "grafana"
ifpass = "6153"
ifdb   = "pi"
ifhost = "127.0.0.1"
ifport = 8086
measurement_name = "system"

# connect to influx
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

def measure():
    # take a timestamp for this measurement
    time = datetime.datetime.utcnow()

    # collect some stats from psutil
    disk = psutil.disk_usage('/')
    mem = psutil.virtual_memory()
    load = psutil.getloadavg()
    temp = psutil.sensors_temperatures()['cpu-thermal'][0].current

    # format the data as a single measurement for influx
    body = [
        {
            "measurement": measurement_name,
            "time": time,
            "fields": {
                "load_1": load[0],
                "load_5": load[1],
                "load_15": load[2],
                "disk_percent": disk.percent,
                "disk_free": disk.free,
                "disk_used": disk.used,
                "mem_percent": mem.percent,
                "mem_free": mem.free,
                "mem_used": mem.used,
                "cpu_temp": temp,
            }
        }
    ]

    # write the measurement
    ifclient.write_points(body)

while True:
    measure()
    time.sleep(1)