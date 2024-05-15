"""
Statemachine zur Schaltung der Ampelsequenz
"""

from machine import Pin
from utime import sleep_ms
from rp2 import PIO, asm_pio, StateMachine


@asm_pio(set_init=(PIO.OUT_LOW, PIO.OUT_LOW, PIO.OUT_LOW))
def ampel():
    label('start')  # Sequenz-Start
    set(pins, 0b00001)  # Rotphase

    set(x, 10)  # Warteschleife Rotphase
    label("loop_R_1")
    set(y, 10)
    label("loop_R_2")
    nop()[31]
    jmp(y_dec, "loop_R_2")
    jmp(x_dec, "loop_R_1")

    set(pins, 0b00011)  # Rot-Gelb Plase

    set(x, 10)  # Warteschleife Rot-Gelb Phase
    label("loop_RG_1")
    set(y, 10)
    label("loop_RG_2")
    nop()[31]
    jmp(y_dec, "loop_RG_2")
    jmp(x_dec, "loop_RG_1")

    set(pins, 0b00100)  # Grünphase

    set(x, 10)  # Warteschleife Grünphase
    label("loop_GR_1")
    set(y, 10)
    label("loop_GR_2")
    nop()[31]
    jmp(y_dec, "loop_GR_2")
    jmp(x_dec, "loop_GR_1")

    set(pins, 0b00010)  # Gelbphase

    set(x, 10)  # Warteschleife Gelbphase
    label("loop_GE_1")
    set(y, 10)
    label("loop_GE_2")
    nop()[31]
    jmp(y_dec, "loop_GE_2")
    jmp(x_dec, "loop_GE_1")

    jmp('start')


sm = StateMachine(0, ampel, freq=1920, set_base=Pin(10))

sm.active(1)
