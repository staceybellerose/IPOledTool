from board import SCL, SDA
import busio
from oled_text import OledText
import getip
import socket

i2c = busio.I2C(SCL, SDA)

# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32)

# Write to the oled

def showIPOnOled():
     eth0ip = getip.get_ip_address('eth0')
     wlan0ip = getip.get_ip_address('wlan0')
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
