# Demoprogramm lässt LED blinken und
# gibt Meldungen auf der Konsole aus.
"""
Erstes MicroPython-Programm zum Test der PyCharm IDE
Stand 24.11.2022 - Python 3.7 mit MicroPython Extension auf PyBoard ( Pico )
"""
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led(1)
    print("LED leuchtet")
    time.sleep(2)
    led(0)
    print("LED abgeschaltet")
    time.sleep(1)