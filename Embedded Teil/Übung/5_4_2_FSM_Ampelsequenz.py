"""
Statemachine zur Schaltung der Ampelsequenz
Die Wartezeit wird durch zwei geschachtelte Schleifen parametriert.
t=x*y*1/freq
Das Hauptprogramm stoppt nach 10 Zyklen (Onboard-LED blinkt)
Die PIOs laufen weiter.
"""

from machine import Pin
import time
from rp2 import PIO, asm_pio, StateMachine


@asm_pio(set_init=(PIO.OUT_LOW, PIO.OUT_LOW, PIO.OUT_LOW))
def ampel():
    label('start')  # Sequenz-Start

    set(pins, 0b00010)  # Gelbphase

    set(x, 10)  # Warteschleife Gelbphase
    label("loop_GE_1")
    set(y, 10)
    label("loop_GE_2")
    nop()[31]
    jmp(y_dec, "loop_GE_2")
    jmp(x_dec, "loop_GE_1")

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

    set(pins, 0b00100)  # Grünphase (Ende Fussgängerphase)

    set(x, 10)  # Warteschleife Grünphase
    label("loop_GR_1")
    set(y, 10)
    label("loop_GR_2")
    nop()[31]
    jmp(y_dec, "loop_GR_2")
    jmp(x_dec, "loop_GR_1")

    jmp('start')


sm = StateMachine(0, ampel, freq=2000, set_base=Pin(10))

sm.active(1)

# Definition der Ein- und Ausgänge
adc = machine.ADC(4)
led = machine.Pin(25, machine.Pin.OUT)
zyklus = 0

# Hauptprogramm

while zyklus < 10:
# Ausgabe der Onboard-Temperatur
    ADC_spannung = adc.read_u16() * (3.3 / 65535)
    temp_in_celsius = 27 - (ADC_spannung - 0.706)/0.001721
    temp_in_fahrenheit = 32+(1.8*temp_in_celsius)
    print("On-Board Temperatur : {} °C {} °F".format(temp_in_celsius, temp_in_fahrenheit))
# Blinken der Onboard-LED
    led(1)
    time.sleep_ms(500)
    led(0)
    print("Zyklus = ", zyklus)
    zyklus += 1
    time.sleep(1)