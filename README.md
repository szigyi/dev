# pi tips

## connect to pi via ssh on localhost
`ssh pi@192.168.1.104`

## To change I2C on raspberry to use adafruit like hat pin numbers for stepper motor
`sudo raspi-config`

## Services
Using influx to store raspberry pi basic metrics. Those metrics get into the DB by the 'tools/system_monitoring_to_influx.py' service.

## Install services
Create a symlink in `/etc/systemd/system` that points to the dev folder's service files. Like so:
   * `cd /etc/systemd/system && sudo ln -s /home/pi/dev/tools/external-temperature-monitoring.service external-temperature-monitoring.service`
   * `system-monitoring.service -> /home/pi/dev/tools/system-monitoring.service`

### Documentation
## Thermometer
Using analoge termometer which means we need specific wiring:
https://magpi.raspberrypi.org/articles/how-to-use-raspberry-pi-temperature-and-light-sensors
