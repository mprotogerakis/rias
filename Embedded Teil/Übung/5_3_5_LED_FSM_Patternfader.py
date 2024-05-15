"""
Statemachine zur Überlagerung zweier LED-Muster per PIO-Assembler
"""
import rp2 as rp2
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import time

button = machine.Pin(20, machine.Pin.IN)


# PIO-Assemblerfunktion
# Preset für 3 Ausgänge (Pin 10 bis 12)
@rp2.asm_pio(set_init=(PIO.OUT_LOW,)*3)
# Das LED-Pattern wird zyklisch eingeschaltet
def led_pattern_1():
    wrap_target()
    set(pins, 0b011)   [4]
    wrap()

# Das LED-Pattern wird zyklisch dem ersten Pattern überlagert
# Jede PIO-Assemblerfunktion muss einer @rp2.asm_pio-Decoration eingeleitet werden.
@rp2.asm_pio(set_init=(PIO.OUT_LOW,)*3)
def led_pattern_2():
    wrap_target()
    set(pins, 0b110)    [4]
    wrap()
# Instanziierung zweier Statemachines, die den Pulse-Effekt durch überlagerung erzeugen sollen
# Beide nutzen den gleichen GPO als Startpin : GPIO 10 mit den beiden Folgepins 11 und 12
# <name> = StateMachine([nummer], freq=[], set_base=Pin([GPIO]))
startpin = Pin(10)
pattern1 = StateMachine(0, led_pattern_1, freq=20001, set_base=startpin)
pattern2 = StateMachine(1, led_pattern_2, freq=20002, set_base=startpin)

# Hauptprogramm : Abfrageschleife für Taster
while True:
    if button.value() == 1:
        pattern1.active(1)
        pattern2.active(1)
        print("Fader läuft")
    else:
        pattern1.active(0)
        pattern2.active(0)
        print("Fader gestoppt")
