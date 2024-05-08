"""
Micropython-Programm zum entprellen (tooglen) einer LED per Taster
Stand 20.10.2023 - Python 3.7 MicroPython Extension auf PyBoard ( Pico )
Taster an GP 20
LED an GP 10
Effekt : Interrupt wird durch Prellen mehrfach aufgerufen -> Zähler springt
https://wokwi.com/projects/397292195290793985
"""
# Importieren der machine-Bibliothek zur Verwendung von Hardwarefunktionen
# https://wokwi.com/projects/397292195290793985
import machine

# Initialisierung der globalen Variablen für den letzten LED-Zustand und Zähler
last_led_state = False  # Zustand der LED speichern
led = machine.Pin(10, machine.Pin.OUT)  # LED an GP10 im Output-Modus
button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)  # Taster an GP20 im Input-Modus
counter = 0  # Zähler für den Hauptprogrammzyklus
isr_counter = 0  # Zähler für die Anzahl der Interrupt-Aufrufe

# Definition der Interrupt-Service-Routine
def toggle_led(pin):
    global last_led_state, isr_counter
    isr_counter += 1  # Erhöhen des Interrupt-Zählers bei jedem Aufruf
    
    # Überprüfung, ob der auslösende Pin der Taster ist
    if pin == button:
        last_led_state = not last_led_state  # Umkehren des LED-Zustandes
        led.value(last_led_state)  # Aktualisieren des LED-Zustands am Pin

# Konfiguration des Interrupts für den Taster
button.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle_led)  # Interrupt bei steigender Flanke

# Endlosschleife zur Ausgabe der Zustände und Zählerstände
while True:
    print("LED :", last_led_state, "   Interrupts:", isr_counter, "   Zähler :", counter)
    counter += 1  # Erhöhen des Hauptprogrammzählers
