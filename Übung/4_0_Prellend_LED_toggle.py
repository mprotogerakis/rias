# Tastersteuerung einer LED
"""
MicroPython-Programm zur Umschaltung einer LED per Taster ohne Entprellung
Stand 26. Juli 2023 - Python 3.7 mit MicroPython Extension auf PyBoard (Pico)
Phänomen : Taster nicht entprellt
"""
import machine
# import utime

led = machine.Pin(10, machine.Pin.OUT, value=0)
button = machine.Pin(20, machine.Pin.IN)
status = 0

while True:
    status = not status
    if button.value() == 1:
        print("Taster gedrückt")
        led(status)
