import sys,time
import machine
from machine import Pin
import network

from http_get import http_get_fn

def control_led(pin_id):
  p = Pin(pin_id,Pin.OUT)
  network_name = input("Enter name of network.\n")
  password = input("Enter password of network.\n")

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.scan()
  print("connecting to network...")
  if wlan.isconnected():
    wlan.disconnect()
  wlan.connect(network_name, password)
  while not wlan.isconnected():
    pass # save power while waiting

  print("Connection successful.")
  print('network config:', wlan.ifconfig())

  while True:
    try:
      data = http_get_fn("http://esp32-project.freevar.com//status.txt")
      print("recieved:", data)
      p.value(data)
      time.sleep(0.1) # Save power between checks on server.
    except:
      pass
