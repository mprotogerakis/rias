# https://wokwi.com/projects/397260102775130113
from machine import ADC, Pin
import time


class DeadTimeBuffer:
    def __init__(self, dead_time_ms):
        self.dead_time_ms = dead_time_ms  # Totzeit in Millisekunden
        self.buffer = []  # Initialisiere eine leere Liste als Buffer

    def update(self, value):
        current_time = time.ticks_ms()
        # Füge das neue Wert-Zeit-Paar am Ende des Buffers hinzu
        self.buffer.append((current_time, value))
      
    def retrieve(self):
        current_time = time.ticks_ms()
        # Filtere alle Werte, deren Zeitstempel mindestens die Totzeit zurückliegt
        valid_values = [val for (time_val, val) in self.buffer if current_time - time_val >= self.dead_time_ms]
        if valid_values:
            # Lösche unbenötigte Werte
            self.buffer = [(time_val, val) for (time_val, val) in self.buffer if current_time - time_val < self.dead_time_ms]
            return valid_values[-1]  # Gib den neuesten gültigen Wert zurück
        else:
            return 0  # Gib 0 zurück, wenn keine gültigen Werte vorliegen

# Konfiguration der Pins (abhängig von deiner spezifischen Hardware)
adc = ADC(Pin(26))  # Konfiguriere ADC auf Pin 26

# Beispiel-Nutzung
buffer = DeadTimeBuffer(dead_time_ms=5000)  # Totzeit von 5000 Millisekunden

time.sleep(0.1)  # Kurze Pause für Stabilität
while True:
    # Lese den analogen Wert
    value = adc.read_u16()
    buffer.update(value)

    # Gib den verarbeiteten Wert aus
    output_value = buffer.retrieve()
    print("Ausgegebener Wert:", output_value)
    time.sleep(0.1)  # Kurze Pause für Stabilität
