# Tasterentprellung zum Togglen einer LED
""""
MicroPython-Programm zum entprellten Togglen einer LED per Taster
Stand 20. Oktober 2023 - Python 3.7 mit MicroPython Extension auf PyBoard ( Pico )
Taster an GP 20
LED an GP 10
Kombination aus Interrupt und Timer zum Entprellen des Tasters.
https://wokwi.com/projects/397293105936129025
"""

# Beispiel von :
# https://www.coderdojotc.org/micropython/advanced-labs/02-interrupt-handlers/

import machine
from machine import Pin
import utime

# Output 10 für LED
led = machine.Pin(10, Pin.OUT)
# Input 20 für Taster
taster = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
# Zähler für Betätigung
gedrueckt = 1
bisher_gedrueckt = 0


def button_handler(pin):
    global gedrueckt
    # disable the IRQ during our debounce check
    taster.irq(handler=None)
    gedrueckt += 1
    # debounce time - we ignore any activity diring this period
    utime.sleep_ms(200)
    # re-enable the IRQ
    taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)


taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
while True:
    # only print on change
    if gedrueckt != bisher_gedrueckt:
        led.toggle()
        if gedrueckt > bisher_gedrueckt + 1:
            print('Interrupts doppelt gezählt. ...Korrektur...')
            gedrueckt = bisher_gedrueckt + 1
        print('Taster gedrückt', gedrueckt, '    Bisher gedrückt :', bisher_gedrueckt)
        bisher_gedrueckt = gedrueckt
