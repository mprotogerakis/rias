import machine
import time

# Pin-Nummer für die LED
led_pin = 2

# Initialisierung des Pins als Ausgang
led = machine.Pin(led_pin, machine.Pin.OUT)

# Schleife zum Blinken der LED
while True:
    led.on()  # LED einschalten
    time.sleep(1)  # 1 Sekunde warten
    led.off()  # LED ausschalten
    time.sleep(1)  # 1 Sekunde warten