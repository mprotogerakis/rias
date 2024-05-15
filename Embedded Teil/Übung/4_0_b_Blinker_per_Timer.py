# Importieren der Pin- und Timer-Klassen aus der machine-Bibliothek
# https://wokwi.com/projects/397294022953684993
from machine import Pin, Timer

# Initialisieren eines Pin-Objekts für die LED am Pin 25 im Output-Modus
led = Pin(10, Pin.OUT)

# Erstellung eines Timer-Objekts zur Steuerung des Blinkintervalls
zeit = Timer()

def blink(timer):
    """
    Diese Funktion wird aufgerufen, um den Zustand der LED umzuschalten.
    Sie verwendet eine XOR-Operation (`not led.value()`) um den aktuellen
    Zustand der LED zu invertieren (ein wird zu aus, aus wird zu ein).
    """
    led.value(not led.value())

# Konfiguration des Timers, um die `blink`-Funktion periodisch aufzurufen.
# mode=Timer.PERIODIC setzt den Timer in den periodischen Modus, was bedeutet,
# dass die Funktion kontinuierlich in dem festgelegten Zeitintervall aufgerufen wird.
# period=500 setzt das Zeitintervall auf 500 Millisekunden (0,5 Sekunden).
# callback=blink gibt an, dass die Funktion `blink` bei jedem Timer-Intervall aufgerufen wird.
zeit.init(mode=Timer.PERIODIC, period=500, callback=blink)
