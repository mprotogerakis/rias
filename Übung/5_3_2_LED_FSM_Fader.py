# https://wokwi.com/projects/397848594970528769
"""
LED-Fader mit PIO-Statemachines
LED1 an GPO 10
Zwei Statemachines mit gering unterschiedlicher Zykluszeit
schalten den LED-Zustand um.
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
sm1 = StateMachine(1, led_on, freq=20001, set_base=Pin(10))
sm2 = StateMachine(2, led_off, freq=20000, set_base=Pin(10))

while True:
    if button.value() == 1:
        sm1.active(1)
        sm2.active(1)
        print("Taster : AN")
    else:
        sm1.active(0)
        sm2.active(1)
        print("Taster : AUS")
