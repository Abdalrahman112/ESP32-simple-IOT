# This file is executed on every boot (including wake-boot from deepsleep)
# notify
print('Booted')

from main import control_led

control_led(22)




