from collections import deque
import time
#programmiere eine Klasse in python die ein totzeitgleid implementiert. dazu sollen parameter über eine methode entgegengenommen werden und zusammen mit der aktuellen zeit in einer fifo-liste abgelegt werden. nachdem eine im konstruktor konfigurierbare totzeit verstrichen ist sollen die werte dann über eine andere methode wieder abgerufen werden. solange die totzeit initial noch nicht vorüber ist, also noch keine daten vorliegen soll der wert 0 ausgegeben werden.


class DeadTimeBuffer:
    def __init__(self, dead_time):
        self.dead_time = dead_time  # Totzeit in Sekunden
        self.buffer = deque()

    def update(self, value):
        current_time = time.time()
        self.buffer.append((current_time, value))
        self._cleanup_buffer()

    def _cleanup_buffer(self):
        current_time = time.time()
        while len(self.buffer) > 1 and current_time - self.buffer[1][0] >= self.dead_time:
            self.buffer.popleft()

    def retrieve(self):
        current_time = time.time()
        valid_values = [val for time_val, val in self.buffer if current_time - time_val >= self.dead_time]
        if valid_values:
            return valid_values[-1]  # Gib den neuesten gültigen Wert zurück
        else:
            return 0  # Gib 0 zurück, wenn keine gültigen Werte vorliegen

# Beispiel-Nutzung
if __name__ == "__main__":
    buffer = DeadTimeBuffer(dead_time=5)  # Totzeit von 5 Sekunden

    # Werte aktualisieren
    buffer.update(10)
    buffer.update(20)

    # Warten bis Totzeit abgelaufen ist
    time.sleep(6)

    # Wert abrufen
    print(buffer.retrieve())  # Sollte 20 ausgeben

    # Wert aktualisieren
    buffer.update(30)

    # Warten bis Totzeit abgelaufen ist
    time.sleep(3)

    # Wert abrufen
    print(buffer.retrieve())  # Sollte 20 ausgeben, da Totzeit des zweiten Werts noch nicht abgelaufen ist

    # Warten bis Totzeit abgelaufen ist
    time.sleep(3)

    # Wert abrufen
    print(buffer.retrieve())  # Sollte 30 ausgeben
