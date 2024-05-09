import unittest
import time
from abc import ABC, abstractmethod

# Hilfsfunktion zur Zeitmessung in Millisekunden
def current_time_ms():
    return int(time.time() * 1000)

# Abstrakte Basisklasse für SISO-Systeme
class SISO(ABC):
    def __init__(self, get_time_callback):
        self.get_time = get_time_callback

    @abstractmethod
    def set_input(self, input_value):
        pass

    @abstractmethod
    def get_output(self):
        pass

# Implementierung des Proportional-Elements
class Proportional(SISO):
    def __init__(self, kp, get_time_callback=current_time_ms):
        super().__init__(get_time_callback)
        self.kp = kp
        self.input_value = None

    def set_input(self, input_value):
        self.input_value = input_value

    def get_output(self):
        return self.kp * self.input_value

# Implementierung des Integrators
class Integrator(SISO):
    def __init__(self, ki, get_time_callback=current_time_ms):
        super().__init__(get_time_callback)
        self.ki = ki
        self.last_update_time = self.get_time()
        self.integral = 0
        self.last_input = 0

    def set_input(self, input_value):
        current_time = self.get_time()
        dt = (current_time - self.last_update_time) / 1000.0  # Umrechnung in Sekunden
        self.integral += self.last_input * dt * self.ki
        self.last_input = input_value
        self.last_update_time = current_time

    def get_output(self):
        self.set_input(self.last_input)  # Aktualisiert das Integral bis zur aktuellen Zeit
        return self.integral

# Implementierung des Differenzierers
class Differentiator(SISO):
    def __init__(self, kd, get_time_callback=current_time_ms):
        super().__init__(get_time_callback)
        self.kd = kd
        self.last_input = None
        self.current_input = None
        self.last_update_time = self.get_time()
        self.current_time = self.get_time()

    def set_input(self, input_value):
        self.last_input = self.current_input
        self.last_update_time = self.current_time
        
        self.current_input = input_value
        self.current_time = self.get_time()
        
    def get_output(self):
        if self.last_input is None:
            return 0
        dt = (self.current_time - self.last_update_time) / 1000.0  # Umrechnung in Sekunden
        if dt > 0:
            return self.kd * (self.current_input - self.last_input) / dt
        return 0

# Kombinierte PID-Regelung
class PIDControl(SISO):
    def __init__(self, kp, ki, kd, get_time_callback=current_time_ms):
        super().__init__(get_time_callback)
        self.P = Proportional(kp, get_time_callback)
        self.I = Integrator(ki, get_time_callback)
        self.D = Differentiator(kd, get_time_callback)

    def set_input(self, input_value):
        self.P.set_input(input_value)
        self.I.set_input(input_value)
        self.D.set_input(input_value)

    def get_output(self):
        return self.P.get_output() + self.I.get_output() + self.D.get_output()

# Unit-Tests für das PID-System
class TestPIDControl(unittest.TestCase):
    def test_pid_control_dynamic_time(self):
        kp = 2.0
        ki = 0.1
        kd = 0.1
        pid = PIDControl(kp, ki, kd, get_time_callback=current_time_ms)
        initial_time = current_time_ms()
        pid.set_input(10)
        while current_time_ms() < initial_time + 1000:  # Warten für 1 Sekunde in Echtzeit
            pass
        pid.set_input(30)
        output = pid.get_output()
        # Berechnung des erwarteten Ausgangs, indem angenommen wird, dass eine Sekunde vergangen ist
        expected_output = 30 * kp + 10 * ki + ((30-10) * kd)  # P + I + D
        self.assertAlmostEqual(output, expected_output, delta=1.0)

if __name__ == '__main__':
    unittest.main()
