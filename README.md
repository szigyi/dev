# pi tips

## Connect to pi via ssh on localhost
`ssh pi@192.168.1.104`

## Shutdown the pi
`sudo shutdown now`

## Services
Using influx to store raspberry pi basic metrics. Those metrics get into the DB by the 'tools/system_monitoring_to_influx.py' service.

## Commands
   * START:  `systemctl start external-temperature-monitoring.service`
   * STOP:   `systemctl stop external-temperature-monitoring.service`
   * Status: `systemctl status external-temperature-monitoring.service`
   * Log:    `journalctl -u system-monitoring.service`

## Install services
Create a symlink in `/etc/systemd/system` that points to the dev folder's service files. Like so:
   * `cd /etc/systemd/system && sudo ln -s /home/pi/dev/tools/external-temperature-monitoring.service external-temperature-monitoring.service`
   * `system-monitoring.service -> /home/pi/dev/tools/system-monitoring.service`

Install dependencies:
   * `pip install influxdb`
   * `pip install psutil`
   * https://github.com/simonmonk/pi_analog

Start your service (Remember that you have to run it first manually to provide the password):
   * `systemctl start external-temperature-monitoring.service`


### Documentation
## Thermometer
Using analoge termometer which means we need specific wiring:
https://magpi.raspberrypi.org/articles/how-to-use-raspberry-pi-temperature-and-light-sensors

Which needs a python lib:
https://github.com/simonmonk/pi_analog


## To change I2C on raspberry to use adafruit like hat pin numbers for stepper motor
`sudo raspi-config`