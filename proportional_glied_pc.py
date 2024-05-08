import unittest
import time

class Proportional:
    def __init__(self, k:float):
        self.k :float= k
        self.value :float = 0.0
    def set_input(self, input_value):
        self.value = input_value

    def get_output(self):
        return self.k * self.value

class TestProportional(unittest.TestCase):
    def test_integration(self):
        prop = Proportional(k=0.1)
        self.assertAlmostEqual(prop.get_output(), 0.0, delta = 0.0)
        prop.set_input(1)
        self.assertAlmostEqual(prop.get_output(), 0.1, delta = 0.0)
        prop.set_input(-1000)
        self.assertAlmostEqual(prop.get_output(), -100, delta = 0.0)
        
        
if __name__ == '__main__':
    unittest.main()
