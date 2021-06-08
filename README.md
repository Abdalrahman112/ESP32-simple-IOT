#Sections
- [Introduction](#Introduction)
- [Usage](#Usage)

#Introduction
This is a simple IOT project used to control a LED on an **ESP32** using **MicroPython**.
After connecting the ESP32 to the USB serial port and rebooting it, the ESP32 asks the user for the network's SSID and password, then it does an http get request on a server uploaded on a free domain to check the state of the LED settings and control it. 
The user can control the state of the LED on the site easily from any web browser.

This project is part of a bigger project, where **mobile** and **desktop apps** will control the state of the LED through overwriting on the site, then the ESP32 controls the LED.

#Usage
To get started, make sure you have the following programs installed:
- python3.
- picocom.
- pyserial.
- esptool.
- The latest micropython binary for ESP32.

[This video](https://www.youtube.com/watch?v=QopRAwUP5ds) is helpful for getting your development environment ready for the project and installing all of the listed programs.

After getting your environment ready and installing micropython on your development board, you should do the following to run the script:
1. Upload your site to a free hosting area.
2. edit the url in the script to be specific to your project like this:
`data = http_get_fn("<Your "status.txt" url>")`
3. edit the port id in the **REPLACE** script to match the one your ESP32 is connected to. For example, this will set the port the script will upload to to port 0:
`port = '/dev/ttyUSB0'`
4. Run the script using the following command:
`python3 REPLACE.py`
5. Use the following command to run the ESP32 and interact with it:
`picocom -b 115200 /dev/ttyUSB0`
Note that this command will only work if the ESP32 is connected to to port 0 and hence should be changed to meet your case.
6. Feel free to tweak the code to your liking, the main thing to remember is that the boot script is what runs after the ESP32 gets rebooted.