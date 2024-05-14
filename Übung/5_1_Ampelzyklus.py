# https://wokwi.com/projects/397848439432073217
# Demoprogramm Ampel
# Gibt Zustände der LEDs auf der Konsole aus.
"""
Ampel-Demo in MicroPython zum Test der PyCharm IDE
Stand 01.12.2022 - Python 3.7 mit MicroPython Extension auf PyBoard ( Pico )
"""
import time
import machine

gruen = machine.Pin(12, machine.Pin.OUT)
gelb = machine.Pin(11, machine.Pin.OUT)
rot = machine.Pin(10, machine.Pin.OUT)
# Ampelinitialisierung
gruen(0)
gelb(0)
rot(1)
while True:
    gruen(1)
    rot(0)
    gelb(0)
    print("Grün")
    time.sleep(2)
    gruen(0)
    gelb(1)
    rot(0)
    print("Gelb")
    time.sleep(2)
    gruen(0)
    gelb(0)
    rot(1)
    print("Rot")
    time.sleep(2)
    gelb(1)
    print("Rotgelb")
    time.sleep(2)
    gelb(0)
    rot(0)
    gruen(1)