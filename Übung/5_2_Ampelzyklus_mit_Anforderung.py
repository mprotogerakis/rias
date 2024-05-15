# https://wokwi.com/projects/397848482333518849
# Demoprogramm Ampel
# Gibt Zustände der LEDs auf der Konsole aus.

"""
Ampel-Demo in MicroPython zum Test der PyCharm IDE
Stand 24.10.2023 - Python 3.7 mit MicroPython Extension auf PyBoard ( Pico )
"""

import time
import machine
import utime

# Definieren der Pins für die Onboard-LEDs
gruen = machine.Pin(12, machine.Pin.OUT)  # Grün LED an Pin 12
gelb = machine.Pin(11, machine.Pin.OUT)  # Gelb LED an Pin 11
rot = machine.Pin(10, machine.Pin.OUT)  # Rot LED an Pin 10

# Definieren des Pins für den Anforderungstaster
taster = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)  # Taster an Pin 20

# Initialisierung der Zähler zum Entprellen des Tasters
gedrueckt = 0
bisher_gedrueckt = 0

# Interrupt Service Routine (ISR) bei Tastendruck
def button_handler(pin):
    global gedrueckt
    # Deaktivieren des Interrupts während der Entprellung
    taster.irq(handler=None)
    # Erhöhen des Zählers für gedrückte Tasten
    gedrueckt += 1
    # Entprellzeit - Ignorieren von Aktivitäten während dieser Zeit
    utime.sleep_ms(800)
    # Reaktivieren des Interrupts
    taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

# Funktion für den Ampelzyklus
def ampelzyklus():
    print('Ampelzyklus angefordert!')
    time.sleep(1)
    # Ampel auf Gelb schalten
    rot.value(0)
    gruen.value(0)
    gelb.value(1)
    print("Gelb")
    time.sleep(2)
    # Ampel auf Rot schalten
    gelb.value(0)
    rot.value(1)
    print("Rot")
    time.sleep(3)
    # Ampel auf Rot-Gelb schalten
    gelb.value(1)
    print("Rotgelb")
    time.sleep(2)
    # Ampel auf Grün schalten
    gelb.value(0)
    rot.value(0)
    gruen.value(1)
    print("Grün")

# Initialisieren der Ampel (alle LEDs aus, Grün an)
rot.value(0)
gelb.value(0)
gruen.value(1)

# Hauptprogrammschleife
while True:
    # Interrupt nur bei fallender Flanke aktivieren, um klemmen des Tasters zu vermeiden
    taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
    while True:
        # Nur bei Änderung des gedrueckt-Zählers drucken
        if gedrueckt != bisher_gedrueckt:
            print('alt:', bisher_gedrueckt, 'neu:', gedrueckt)
            # Deaktivieren des Taster-Interrupts
            taster.irq(handler=None)
            # Starten des Ampelzyklus
            ampelzyklus()
            # Reaktivieren des Interrupts
            taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
            # Korrektur des Zählers bei mehrfachen (nested) Interrupts
            # Nur ein Ereignis wird gezählt
            if gedrueckt > bisher_gedrueckt + 1:
                gedrueckt = bisher_gedrueckt + 1
            # Aktualisieren des bisher_gedrueckt-Zählers
            bisher_gedrueckt = gedrueckt