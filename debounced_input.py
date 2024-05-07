# https://wokwi.com/projects/397250238324892673
from machine import Pin, Timer

class DebouncedInput:
    def __init__(self, button: Pin, debounce_time_ms: int, callback) -> None:
        """Initialisiert den DebouncedInput mit einem Pin-Objekt, Entprell-Zeit und einem Callback.

        Args:
            button (Pin): Das Pin-Objekt, das für den Eingang verwendet wird.
            debounce_time_ms (int): Die Entprellzeit in Millisekunden.
            callback (Callable[[Timer], None]): Die Funktion, die aufgerufen wird, wenn der Timer abläuft.
        """
        self.button = button
        self.debounce_time_ms = debounce_time_ms
        self.timer = Timer()
        self.callback = callback
        self.button.irq(handler=self.debounce, trigger=Pin.IRQ_FALLING)

    def tipped(self, timer: Timer) -> None:
        """Wird aufgerufen, wenn der Timer abläuft, und überprüft den Zustand des Buttons."""
        if not self.button.value():  # Prüfen, ob der Button noch gedrückt ist
            self.callback(timer)

    def debounce(self, pin: Pin) -> None:
        """IRQ-Handler, der einen Timer startet, um das Bouncing zu vermeiden."""
        self.timer.init(mode=Timer.ONE_SHOT, period=self.debounce_time_ms, callback=self.tipped)

# Callback-Funktion, die außerhalb der Klasse definiert wird
def tipped(timer: Timer) -> None:
    """Callback-Funktion, die ausgelöst wird, wenn der Button tatsächlich gedrückt ist."""
    print("Button pressed!")

# Beispiel für die Verwendung der DebouncedInput-Klasse
import utime
from machine import Pin

# Erstellen eines Pin-Objekts
button_pin = Pin(7, Pin.IN, Pin.PULL_UP)
# Instanziieren der DebouncedInput-Klasse mit dem externen Callback
debounced_button = DebouncedInput(button_pin, 200, tipped)

while True:
    utime.sleep(1)  # Kurze Pause, um die CPU-Last zu reduzieren
