#!/usr/bin/python3

#
# J.A. Korten
# July 7, 2021
# Script to show hostname, eth0 and wlan0 addresses on small oled
#
# Don't forget to sudo chmod +x updateshowip.py on the script and add it as a cronjob
#
# we will run it as systemd process to avoid startup issues
# see also: http://iltabiai.github.io/raspberry%20pi/python/linux/ubuntu/telegram/2020/05/08/python-systemd.html

import schedule
import time
import schedule
import time
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "reinstall", package])

from board import SCL, SDA
'''
ToDo: fix auto installing blinka.
except:
    # adafruit-blinka
    print("board package not found, trying to install adafruit-blinka")
    install("adafruit-blinka")
    try:
        from board import SCL, SDA
    except:
        print("Still an issue with board package. Aborting.")
'''
print("IPOledTool script was executed")
print("This script prints hostname, eth0 and wlan0 addresses on small oled")
print("Values are update every second")
print("J.A. Korten - 2021")
print()
print("Initial values:")


import busio
from oled_text import OledText
from more_scripts import getip
import socket

try:
    i2c = busio.I2C(SCL, SDA)
except:
    print("I2C error, maybe you forgot to enable it through raspi-config?")
    exit()
# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32)

# Write to the oled

def showIPOnOled():
     eth0ip = get_ip_address('eth0')
     wlan0ip = get_ip_address('wlan0')
     hostname = socket.gethostname()
     oled.text("H: " + hostname, 1)
     oled.text("E: " + eth0ip, 2)
     oled.text("W: " + wlan0ip, 3)
     #print("Update...") # shows that values are indeed updated...

def printInitialValues():
     eth0ip = getip.get_ip_address('eth0')
     wlan0ip = getip.get_ip_address('wlan0')
     hostname = socket.gethostname()
     print("Hostname: " + hostname)
     print("Ethernet: " + eth0ip)
     print("Wireless: " + wlan0ip)

printInitialValues()
print()

import socket
import fcntl
import struct



def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])
    except:
        return "n/a"

def perform_task():
    showIPOnOled()

schedule.every(1).seconds.do(perform_task)

while (1):
    schedule.run_pending()
    time.sleep(1)
