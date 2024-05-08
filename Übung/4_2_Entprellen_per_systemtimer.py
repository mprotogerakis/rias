# Demoprogramm Tasterentprellung mit Timer-Ticks
"""
Tasterentprellung in MicroPython zum Test der PyCharm IDE
Stand 03.08.2023 - Python 3.7 mit MicroPython Extension auf PyBoard (Pico)
Button_1 auf GPI-Pin 20
LED_1 auf GPO 10
Funktion :
"entprellen" setzt die Entprellzeit in ms.
Wird Button_1 länger betätigt, als per "entprellzeit" vorgegeben,
Blinkt LED_1 10 mal kurz auf.
Statusmeldungen werden in der Konsole ausgegeben.
Nachteil : Sleep hält main für Millisekunden an -> ineffizient
https://wokwi.com/projects/397297228139688961
"""

from machine import Pin
import time
taster = Pin(20, Pin.IN)
led = Pin(10, Pin.OUT)
entprellzeit = 100
while True:
    while taster.value() == 0:
        # print("ungedrückt")
        # print("ticks :", t)
        pass
    # Intervallzähler t wird laufend auf Systemticks aktualisiert
    t = time.ticks_ms()
    # Hauptprogramm für 1 ms anhalten, solange Taster unbetätigt ist.
    # Dadurch erhöht sich die Differenz zwischen Systemticks und dem Merker t
    # jeweils um 1.
    time.sleep_ms(1)
    while taster.value() == 1:
        # print("gedrückt")
        pass
    # Differenzberechnung zwischen aktuellem Systemtickzähler und Merker t
    t = time.ticks_diff(time.ticks_ms(), t)
    if t < entprellzeit:
        print("zu kurz gedrückt ! ")
    # Sobald die Entprellzeit überschritten ist, gilt der Taster als sicher betätigt.
    # Die LED blinkt 10 mal zur Quittierung
    else:
        print("Das war lang genug !")
        for i in range(10):
            led.on()
            time.sleep_ms(500)
            led.off()
            time.sleep_ms(500)
        # Aktualisierung von t
        t = time.ticks_ms()