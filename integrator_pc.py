#für die implementierung eines pid reglers in python soll ein integratorelement als klasse implemeniert werden. eine methode soll dem setzen des integratoreingangs dienen. im konstruktor sollen die nötigen konstanten übergeben werden. eine methode dient dem abrufen des wertes. bitte schreibe den code einschliesslich unit test

import unittest
import time

class Integrator:
    def __init__(self, ki):
        self.ki = ki  # Integrationskonstante
        self.last_update_time = time.time()
        self.integral = 0
        self.last_input = 0

    def set_input(self, input_value):
        current_time = time.time()
        dt = current_time - self.last_update_time
        self.integral = self.integral + self.last_input * dt * self.ki
        self.last_input = input_value
        self.last_update_time = current_time

    def get_output(self):
        current_time = time.time()
        dt = current_time - self.last_update_time
        self.integral = self.integral + self.last_input * dt * self.ki
        self.last_update_time = current_time
        return self.integral

class TestIntegrator(unittest.TestCase):
    def test_integration(self):
        integrator = Integrator(ki=0.1)
        self.assertAlmostEqual(integrator.get_output(), 0.0, delta = 0.1)
        integrator.set_input(1)
        time.sleep(1)  # Eine Sekunde warten ->1
        self.assertAlmostEqual(integrator.get_output(), 0.1, delta = 0.1)
        integrator.set_input(2)
        time.sleep(1)  # Eine Sekunde warten ->3
        self.assertAlmostEqual(integrator.get_output(), 0.3, delta = 0.1)
        integrator.set_input(3)
        self.assertAlmostEqual(integrator.get_output(), 0.3, delta = 0.1)
        time.sleep(1)  # Eine Sekunde warten ->6
        self.assertAlmostEqual(integrator.get_output(), 0.6, delta = 0.1)

        time.sleep(1)  # Eine Sekunde warten
        self.assertAlmostEqual(integrator.get_output(), 0.9, delta = 0.1)
        integrator.set_input(-1)
        time.sleep(1)  # Eine Sekunde warten
        self.assertAlmostEqual(integrator.get_output(), 0.8, delta = 0.1)
      
if __name__ == '__main__':
    unittest.main()
