import asyncio

# Eine asynchrone Funktion, die simuliert, dass eine LED blinkt
async def blink_led(period_ms: int) -> None:
    state = False  # Anfangszustand der LED
    while True:
        state = not state  # Toggle LED state
        print(f"LED {'on' if state else 'off'}")  # Drucke den aktuellen Zustand der LED
        await asyncio.sleep(period_ms / 1000)  # Warte für die angegebene Periode, umgerechnet in Sekunden

# Eine asynchrone Funktion, die regelmäßig Nachrichten ausgibt
async def print_messages(interval_ms: int) -> None:
    counter: int = 0
    while True:
        print(f"Message {counter}")
        counter += 1
        await asyncio.sleep(interval_ms / 1000)  # Warte für das angegebene Intervall, umgerechnet in Sekunden

# Die Hauptfunktion, die die anderen asynchronen Funktionen startet
async def main() -> None:
    # Erstelle Tasks für das Blinken einer LED und das Ausgeben von Nachrichten
    blink_task = asyncio.create_task(blink_led(500))  # Simuliertes Blinken einer LED alle 500 ms
    message_task = asyncio.create_task(print_messages(700))  # Ausgeben von Nachrichten alle 700 ms
    await asyncio.sleep(10)  # Läuft 10 Sekunden lang
    blink_task.cancel()
    message_task.cancel()

# Führe die Hauptfunktion aus
asyncio.run(main())
