# pi tips
 
## Discover devices on local network
   * `ifconfig | grep broadcast`
   * `arp -a`

## Connect to pi via ssh on localhost
`ssh pi@192.168.1.104`

## Shutdown the pi
`sudo shutdown now`

## Use pi aliases
Symlink the .bash_aliases file to your home folder, like wise:
   * `cd ~ &&  sudo ln -s /home/pi/dev/.bash_aliases .bash_aliases`
And then invoke the functions from `.bashrc` or other profile file.
   * `pi_welcome`
   * `pi_cmds`

## Auto-Hotspot
https://github.com/RaspberryConnect/AutoHotspot-Installer

## Services
Using influx to store raspberry pi basic metrics. Those metrics get into the DB by the 'tools/system_monitoring_to_influx.py' service.

## Commands
   * START
      * `systemctl start system-monitoring.service`
      * `systemctl start external-temperature-monitoring.service`
   * STOP
      * `systemctl stop system-monitoring.service`
      * `systemctl stop external-temperature-monitoring.service`
   * Status
      * `systemctl status system-monitoring.service`
      * `systemctl status external-temperature-monitoring.service`
   * Log
      * `journalctl -u system-monitoring.service`
      * `journalctl -u external-temperature-monitoring.service`

## Install services
Create a symlink in `/etc/systemd/system` that points to the dev folder's service files. Like so:
   * `cd /etc/systemd/system && sudo ln -s /home/pi/dev/tools/external-temperature-monitoring.service external-temperature-monitoring.service`
   * You should see: `system-monitoring.service -> /home/pi/dev/tools/system-monitoring.service`
Install dependencies:
   * `pip install influxdb`
   * `pip install psutil`
   * Install https://github.com/simonmonk/pi_analog
      * `$ git clone https://github.com/simonmonk/pi_analog.git`
      * `cd pi_analog`
      * `sudo python3 setup.py install`
And then start it
   * `systemctl start system-monitoring.service`
Eventually, enable it so it will be started after system has booted
   * `systemctl enable system-monitoring.service`


### Documentation
## Thermometer
Using analoge termometer which means we need specific wiring:
https://magpi.raspberrypi.org/articles/how-to-use-raspberry-pi-temperature-and-light-sensors

Which needs a python lib:
https://github.com/simonmonk/pi_analog


## To change I2C on raspberry to use adafruit like hat pin numbers for stepper motor
`sudo raspi-config`
