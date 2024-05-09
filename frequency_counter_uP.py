#https://wokwi.com/projects/397422208221595649
from machine import Pin, PWM
import time

# Initialisiere GP27 als Ausgang für den Frequenzgenerator
pwm_pin: PWM = PWM(Pin(27))

# Konfiguriere den PWM für 1 kHz Frequenz
def setup_pwm(frequency: int) -> None:
    pwm_pin.freq(frequency)
    pwm_pin.duty_u16(32768)  # Setze das Tastverhältnis auf 50%

# Initialisiere GP21 als Eingang für den Frequenzzähler
counter_pin: Pin = Pin(21, Pin.IN)

# Variable zum Speichern der Zählung der Frequenz
frequency_count: int = 0

# IRQ Handler Funktion zum Zählen der Flankenwechsel
def handle_interrupt(pin: Pin) -> None:
    global frequency_count
    frequency_count += 1

# Funktion zum Zählen der Frequenz
def frequency_counter(duration: int) -> int:
    global frequency_count
    frequency_count = 0  # Reset count
    counter_pin.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
    
    time.sleep(duration)  # Zähle für die spezifizierte Dauer in Sekunden
    counter_pin.irq(handler=None)  # Deaktiviere IRQ
    
    return frequency_count

# Konfiguriere den PWM-Ausgang
setup_pwm(1000)  # 1 kHz

try:
    while True:
        # Messe die Frequenz am Eingangspunkt
        frequency: int = frequency_counter(1)  # Misst für 1 Sekunde
        print(f"Gemessene Frequenz: {frequency} Hz")
        time.sleep(1)  # Warte eine Sekunde zwischen den Messungen

except KeyboardInterrupt:
    # Bereinige, wenn das Programm unterbrochen wird
    pwm_pin.deinit()  # Stoppe den PWM
    print("Programm beendet.")
