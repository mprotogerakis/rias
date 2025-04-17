# Version für PC mit Unittest
# Variante für Micropython siehe https://wokwi.com/projects/397260102775130113
import time


class DeadTimeBuffer:
    def __init__(self, dead_time_ms):
        self.dead_time_ms = dead_time_ms  # Totzeit in Millisekunden
        self.buffer = []  # Initialisiere eine leere Liste als Buffer

    def update(self, value):
        current_time = int(time.time() * 1000)  # Umwandlung in Millisekunden
        self.buffer.append((current_time, value))

    def retrieve(self):
        current_time = int(time.time() * 1000)
        valid_values = [val for (time_val, val) in self.buffer if current_time - time_val >= self.dead_time_ms]
        if valid_values:
            # Lösche unbenötigte Werte
            self.buffer = [(time_val, val) for (time_val, val) in self.buffer if
                           current_time - time_val < self.dead_time_ms]
            return valid_values[-1]  # Gib den neuesten gültigen Wert zurück
        else:
            return 0  # Gib 0 zurück, wenn keine gültigen Werte vorliegen


import unittest


class TestDeadTimeBuffer(unittest.TestCase):

    def test_retrieve(self):
        buffer = DeadTimeBuffer(dead_time_ms=1000)  # Totzeit von 1 Sekunde
        start_time = int(time.time() * 1000)

        # Update the buffer with values
        buffer.update(100)
        time.sleep(0.5)  # 500 ms Pause
        buffer.update(200)
        time.sleep(0.5)  # weitere 500 ms Pause
        buffer.update(300)

        self.assertEqual(buffer.retrieve(), 100)

        time.sleep(0.6)
        self.assertEqual(buffer.retrieve(), 200)

        time.sleep(0.5)
        self.assertEqual(buffer.retrieve(), 300)


if __name__ == "__main__":
    unittest.main()
