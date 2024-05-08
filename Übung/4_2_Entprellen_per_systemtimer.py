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
https://wokwi.com/projects/397293737414864897
"""

from machine import Pin
import time

taster = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(10, Pin.OUT)
entprellzeit = 100  # Entprellzeit in ms

while True:
    # Warte auf das Drücken des Tasters
    while taster.value() == 0:
        pass

    # Warte kurz, um Prellen zu vermeiden
    time.sleep_ms(20)

    # Bestätige, dass der Taster immer noch gedrückt ist
    if taster.value() == 0:
        startzeit = time.ticks_ms()

        # Warte, bis der Taster losgelassen wird
        while taster.value() == 0:
            pass

        # Warte erneut kurz, um das Loslassen-Prellen zu vermeiden
        time.sleep_ms(20)

        # Bestätige, dass der Taster wirklich losgelassen wurde
        if taster.value() == 1:
            gedrueckte_zeit = time.ticks_diff(time.ticks_ms(), startzeit)

            if gedrueckte_zeit < entprellzeit:
                print("Zu kurz gedrückt!")
            else:
                print("Das war lang genug!")
                for i in range(10):
                    led.on()
                    time.sleep_ms(50)
                    led.off()
                    time.sleep_ms(50)
