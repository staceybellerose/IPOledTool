#!/usr/bin/python3

"""
Author: J.A. Korten, July 7, 2021
Modified: Stacey Adams, October 29, 2022

Script to show hostname, eth0 and wlan0 addresses on small oled.

Don't forget to sudo chmod +x updateshowip.py on the script and add it as a cronjob.

We will run it as systemd process to avoid startup issues; see also:
http://iltabiai.github.io/raspberry%20pi/python/linux/ubuntu/telegram/2020/05/08/python-systemd.html
"""

import time
import socket
import fcntl
import struct
import schedule
import busio
from board import SCL, SDA
from oled_text import OledText

print("IPOledTool script was executed")
print("This script prints hostname, eth0 and wlan0 addresses on small oled")
print("Values are updated every second")
print("J.A. Korten - 2021; Stacey Adams - 2022")
print()

try:
    I2C = busio.I2C(SCL, SDA)
except RuntimeError:
    print("I2C error, maybe you forgot to enable it through raspi-config?")
    exit()

# Create the display, pass its pixel dimensions
OLED = OledText(I2C, 128, 32)

SIOCGIFADDR = 0x8915

def get_ip_address(ifname):
    """Get the IP address of the provided interface."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ifreq = struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    try:
        res = fcntl.ioctl(sock.fileno(), SIOCGIFADDR, ifreq)
    except OSError:
        return 'n/a'
    return socket.inet_ntoa(res[20:24])

# Collect the data to display
def collect_data():
    """Collect the IP addresses and host name."""
    eth0ip = get_ip_address('eth0')
    wlan0ip = get_ip_address('wlan0')
    hostname = socket.gethostname()
    return (eth0ip, wlan0ip, hostname)

# Write to the oled
def show_ip_on_oled():
    """Write the IP addresses and host name to the OLED."""
    (eth0ip, wlan0ip, hostname) = collect_data()
    OLED.text("H: " + hostname, 1)
    OLED.text("E: " + eth0ip, 2)
    OLED.text("W: " + wlan0ip, 3)
    #print "Update..." # shows that values are indeed updated...

def print_initial_values():
    """Print the initial values of the IP addresses and host name."""
    (eth0ip, wlan0ip, hostname) = collect_data()
    print("Initial values:")
    print("Hostname: " + hostname)
    print("Ethernet: " + eth0ip)
    print("Wireless: " + wlan0ip)

print_initial_values()
print()

schedule.every(1).seconds.do(show_ip_on_oled)

while True:
    schedule.run_pending()
    time.sleep(1)
