# Tastersteuerung einer LED
""""
MicroPython-Programm zur Steuerung eine LED per Taster
Stand 26. Juli 2023 - Python 3.7 mit MicroPython Extension auf PyBoard ( Pico )
"""
import machine

led = machine.Pin(10, machine.Pin.OUT)
button = machine.Pin(20, machine.Pin.IN)

while True:
    if button.value() == 1:
        led(1)
        print("Taster : AN")
    else:
        led(0)
        print("Taster : AUS")
