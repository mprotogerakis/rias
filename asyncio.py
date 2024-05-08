# https://wokwi.com/projects/397303247884411905
import uasyncio as asyncio
from machine import Pin

# Eine asynchrone Funktion, die eine LED an einem bestimmten Pin blinken lässt
async def blink_led(pin: int, period_ms: int) -> None:
    # Initialisiere den Pin als Ausgang
    led = Pin(pin, Pin.OUT)
    while True:
        led.value(not led.value())  # Toggle LED state
        await asyncio.sleep_ms(period_ms)  # Warte für die angegebene Periode

# Eine asynchrone Funktion, die regelmäßig Nachrichten ausgibt
async def print_messages(interval_ms: int) -> None:
    counter: int = 0
    while True:
        print(f"Message {counter}")
        counter += 1
        await asyncio.sleep_ms(interval_ms)  # Warte für das angegebene Intervall

# Die Hauptfunktion, die die anderen asynchronen Funktionen startet
async def main() -> None:
    # Erstelle Tasks für das Blinken einer LED und das Ausgeben von Nachrichten
    asyncio.create_task(blink_led(7, 500))  # Annahme: GPIO2 für die LED
    asyncio.create_task(print_messages(700))
    await asyncio.sleep(10)  # Läuft 10 Sekunden lang

# Führe die Hauptfunktion aus
asyncio.run(main())
