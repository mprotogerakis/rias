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
# Onboad-LEDs
gruen = machine.Pin(12, machine.Pin.OUT)
gelb = machine.Pin(11, machine.Pin.OUT)
rot = machine.Pin(10, machine.Pin.OUT)
# Anforderungstaster : GPI 20
taster = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
# Zähler zum Entprellen
gedrueckt = 0
bisher_gedrueckt = 0


# ISR bei Tastendruck
def button_handler(pin):
    global gedrueckt
    # disable the IRQ during our debounce check
    taster.irq(handler=None)
    gedrueckt += 1
    # debounce time - we ignore any activity diring this period
    utime.sleep_ms(800)
    # re-enable the IRQ
    taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)


def ampelzyklus():
    print('Ampelzyklus angefordert !')
    time.sleep(1)
    rot(0)
    gruen(0)
    gelb(1)
    print("Gelb")
    time.sleep(2)
    gelb(0)
    rot(1)
    print("Rot")
    time.sleep(3)
    gelb(1)
    print("Rotgelb")
    time.sleep(2)
    gelb(0)
    rot(0)
    gruen(1)
    print("Grün")


# Ampelinitialisierung ( Alle Seiten Rot ! )
rot(0)
gelb(0)
gruen(1)
while True:
    # Interrupt nur bei fallender Flanke, damit ein klebender Taster die Kreuzung nicht blockiert
    taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
    while True:
        # only print on change
        if gedrueckt != bisher_gedrueckt:
            print('alt : ', bisher_gedrueckt, 'neu : ', gedrueckt)
            # Deaktivierung des Tasterinterrupts
            taster.irq(handler=None)
            ampelzyklus()
            # Reaktivierung des Interrupts
            taster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
            # Korrektur des Zählers bei mehrfachen (nested) Interrupts
            # Nur ein Ereignis wird gezählt
            if gedrueckt > bisher_gedrueckt + 1:
                gedrueckt = bisher_gedrueckt + 1
            bisher_gedrueckt = gedrueckt
