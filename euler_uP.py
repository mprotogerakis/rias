# https://wokwi.com/projects/397307016234341377

from machine import Pin
from utime import sleep
from machine import Pin, PWM
import uasyncio as asyncio

sleep(0.5)
print("Hello, Pi Pico!")



# Konstanten
k: float = 1.0  # Federkonstante
dt: float = 0.01  # Zeitschritt in Sekunden

# Anfangsbedingungen
x: float = 1.0  # Anfangsposition
v: float = 0.0  # Anfangsgeschwindigkeit

# PWM-Konfiguration
pwm_pin: Pin = Pin(10, Pin.OUT)
pwm: PWM = PWM(pwm_pin, freq=1000)

async def simulate() -> None:
    global x, v
    while True:
        # Euler-Verfahren zur Berechnung der nächsten Werte
        new_v: float = v - k * x * dt
        new_x: float = x + v * dt

        # Update der aktuellen Werte
        x, v = new_x, new_v

        # Konvertiere Position x in einen PWM-Wert (einfaches Beispiel)
        pwm_value: int = int((x + 1.1) * pow(2,13))  # Skalierung und Offset für PWM
        print (f"x={pwm_value}")
        pwm.duty_u16(pwm_value)

        # Warte bis zum nächsten Zeitschritt
        await asyncio.sleep(dt)

async def main() -> None:
    try:
        await simulate()
    finally:
        pwm.deinit()  # PWM abschalten und aufräumen

# Start der asyncio Event-Loop
asyncio.run(main())
