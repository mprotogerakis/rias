"""
Statemachine zur Ansteuerung eines GPO (Pin 10) mit Blinkfunktion
LED1 an GPO 10
"""
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import time

button = machine.Pin(20, machine.Pin.IN)

@asm_pio(set_init=PIO.OUT_LOW)
def led_off():
    set(pins, 0)

@asm_pio(set_init=PIO.OUT_LOW)
def led_on():
    set(pins, 1)

# Instanziierung zweier Statemachines
# <name> = StateMachine([nummer], freq=[], set_base=Pin([GPIO]))
roton = StateMachine(1, led_on, freq=20001, set_base=Pin(10))
rotoff = StateMachine(2, led_off, freq=20000, set_base=Pin(10))
gelbon = StateMachine(3, led_on, freq=20001, set_base=Pin(11))
gelboff = StateMachine(4, led_off, freq=20000, set_base=Pin(11))
gruenon = StateMachine(5, led_on, freq=20001, set_base=Pin(12))
gruenoff = StateMachine(6, led_off, freq=20000, set_base=Pin(12))

while True:
    if button.value() == 1:
        roton.active(1)
        rotoff.active(1)
        gelbon.active(0)
        gelboff.active(0)
        print("Rot fadet")
    else:
        roton.active(0)
        rotoff.active(0)
        gelbon.active(1)
        gelboff.active(1)
        print("Gelb fadet")

#sm1.active(1)
# sm2.active(1)