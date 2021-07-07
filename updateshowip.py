#!/usr/bin/python3

#
# J.A. Korten
# July 7, 2021
# Script to show hostname, eth0 and wlan0 addresses on small oled
#
# Don't forget to sudo chmod +x updateshowip.py on the script and add it as a service
#
# we will run it as systemd process to avoid startup issues
# see also: http://iltabiai.github.io/raspberry%20pi/python/linux/ubuntu/telegram/2020/05/08/python-systemd.html

import schedule
import time
from board import SCL, SDA
import busio
from oled_text import OledText
import getip
import socket
import fcntl
import struct

i2c = busio.I2C(SCL, SDA)

# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32) # taylor to your own needs

def printInitialInfo():
    print("IPOledTool script was executed")
    print("This script prints hostname, eth0 and wlan0 addresses on small oled")
    print("Values are update every second")
    print("J.A. Korten - 2021, V1.0")
    print()
    print("Initial values:")
    printInitialValues(hostname, eth0ip, wlan0ip)
    print()

# helper method to get IP address of addapter based on ifname (lo, eth0, wlan0 typically)
def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])
    except:
        return "n/a"

def showValuesOnOled(hostname, eth0ip, wlan0ip):
     # Write to the oled
     oled.text("H: " + hostname, 1)
     oled.text("E: " + eth0ip, 2)
     oled.text("W: " + wlan0ip, 3)
     #print("Update...") # shows that values are indeed updated...

def printInterfaceValues(hostname, eth0ip, wlan0ip):
     eth0ip = getip.get_ip_address('eth0')
     wlan0ip = getip.get_ip_address('wlan0')
     hostname = socket.gethostname()
     print("Hostname: " + hostname)
     print("Ethernet: " + eth0ip)
     print("Wireless: " + wlan0ip)


eth0ip = getip.get_ip_address('eth0')
wlan0ip = getip.get_ip_address('wlan0')
hostname = socket.gethostname()
printInitialInfo(hostname, eth0ip, wlan0ip)

def perform_task():
    #update values:
    eth0ip = getip.get_ip_address('eth0')
    wlan0ip = getip.get_ip_address('wlan0')
    hostname = socket.gethostname()
    showValuesOnOleds(hostname, eth0ip, wlan0ip)

schedule.every(1).seconds.do(perform_task)

while (1):
    schedule.run_pending()
    time.sleep(1)
