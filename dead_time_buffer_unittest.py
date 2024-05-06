# bitte ergänze die klasseDeadTimeBuffer um einen unittest
from collections import deque
import time
import unittest
from time import sleep

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

class TestDeadTimeBuffer(unittest.TestCase):
    def test_buffer_with_dead_time(self):
        buffer = DeadTimeBuffer(dead_time=5)

        buffer.update(10)
        buffer.update(20)
        self.assertEqual(buffer.retrieve(), 0)  

        sleep(6)
        self.assertEqual(buffer.retrieve(), 20)  

        buffer.update(30)
        self.assertEqual(buffer.retrieve(), 20) 

        sleep(3)
        self.assertEqual(buffer.retrieve(), 20)  

        sleep(3)
        self.assertEqual(buffer.retrieve(), 30)  

        sleep(3)
        self.assertEqual(buffer.retrieve(), 30)  

if __name__ == '__main__':
    unittest.main()