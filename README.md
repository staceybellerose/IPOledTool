# IPOledTool

Tool to put hostname and ip's on an Oled display of a Pi

- updateshowip.py
- service/ipoledtool.service

We tested this code with both Raspberry Pi 3 and 4's.
We use it in conjunction with e.g. Homebridge and Octopi servers that are not connected to any screen apart from the simple Oled displays.

Oled display used was a: <br>
"AZDelivery 0.91" OLED Display I2C SSD1306 Chip 128 x 32 Pixel I2C Screen Display Module with White Characters".

However, also I2C SSD1306 OLED displays should work.

## Step A. Prepare python files

Two options:<br>
I. Through git clone<br>
II. Manually<br>

### I. Git clone option

1. Clone this repository: 

        git clone https://github.com/jakorten/IPOledTool.git
        
2. CD to that folder:

        cd ~/IPOledTool

3. Make updateshowip.py executable:

        sudo chmod +x updateshowip.py

4. Check the script:

        ./updateshowip.py

5. Add possibly missing libraries using pip3 (now you are supposed to use: sudo python3 -m pip install some_python_library_name)


### II. Manual option

1. Create a folder:

        mkdir ~/IPOledTool

2. CD to that folder:

        cd ~/IPOledTool

3. Download updateshowip.py

4. Make updateshowip.py executable:

        sudo chmod +x updateshowip.py

5. Check the script:

        ./updateshowip.py

6. Add possibly missing libraries using pip3 (now you are supposed to use: sudo python3 -m pip install some_python_library_name).
You could simply issue to install all needed libraries (see down below):

        pip3 install -r requirements.txt

## Step B. Create a Service

Create a service using ipoledtool.service
(see: https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)

1. Copy ipoledtool.service to /lib/systemd/system/

        sudo cp service/ipoledtool.service /lib/systemd/system

2. Make service exacutable

        sudo chmod 644 /lib/systemd/system/ipoledtool.service

3. Restart systemctl daemon:

        sudo systemctl daemon-reload
        sudo systemctl enable ipoledtool.service
        
        
## Libraries

The script uses the following libraries (install with pip3):
- schedule (pip3 install schedule)
- board (pip3 install board)
- busio (pip3 install adafruit-blinka)
- oled_text (pip3 install oled_text)
- PIL (pip3 install Pillow)

Or simply run:

        pip3 install -r requirements.txt

If you get the message that pip3 can not be found then first:

        sudo apt install python3-pip
