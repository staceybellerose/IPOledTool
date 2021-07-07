# IPOledTool

Tool to put hostname and ip's on an Oled display of a Pi

- updateshowip.py
- service/ipoledtool.service

## Step A. Prepare python files

1. Create a folder:
    mkdir ~/IPOledTool
2. CD to that folder:
    cd ~/IPOledTool
3. Download updateshowip.py
4. Make updateshowip.py executable:
    sudo chmod +x updateshowip.py
5. Check the script:
    ./updateshowip.py
6. Add possibly missing libraries using pip3 (now you are supposed to use: sudo python3 -m pip install some_python_library_name)

## Step B. Create a Service

Create a service using ipoledtool.service
(see: https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)

1. Copy ipoledtool.service to /lib/systemd/system/

2. Make service exacutable

    sudo chmod 644 /lib/systemd/system/ipoledtool.service

3. Restart systemctl daemon:

    sudo systemctl daemon-reload
    sudo systemctl enable ipoledtool.service
