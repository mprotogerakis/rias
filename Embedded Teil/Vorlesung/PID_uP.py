# https://wokwi.com/projects/397425111351428097
from machine import Pin, ADC, PWM
import utime

# Klassen für Proportional, Integrator, Differentiator und PIDControl
class SISO:
    def __init__(self, get_time_callback):
        self.get_time = get_time_callback

    def set_input(self, input_value):
        pass

    def get_output(self):
        pass

class Proportional(SISO):
    def __init__(self, kp, get_time_callback):
        super().__init__(get_time_callback)
        self.kp = kp
        self.input_value = 0

    def set_input(self, input_value):
        self.input_value = input_value

    def get_output(self):
        return self.kp * self.input_value

class Integrator(SISO):
    def __init__(self, ki, get_time_callback):
        super().__init__(get_time_callback)
        self.ki = ki
        self.last_update_time = self.get_time()
        self.integral = 0
        self.last_input = 0

    def set_input(self, input_value):
        current_time = self.get_time()
        dt = (current_time - self.last_update_time) / 1000.0
        self.integral += self.last_input * dt * self.ki
        self.last_input = input_value
        self.last_update_time = current_time

    def get_output(self):
        self.set_input(self.last_input)
        return self.integral

class Differentiator(SISO):
    def __init__(self, kd, get_time_callback):
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
        dt = (self.current_time - self.last_update_time) / 1000.0
        if dt > 0:
            return self.kd * (self.current_input - self.last_input) / dt
        return 0

class PIDControl(SISO):
    def __init__(self, kp, ki, kd, get_time_callback):
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

# Setup für ADC (Analog-Digital-Wandler) für Potentiometer
adc_set_point = ADC(Pin(26))
adc_feedback = ADC(Pin(27))

# Setup für das Servo
servo = PWM(Pin(21))
servo.freq(50)  # Servo erwartet eine Frequenz von 50Hz

# Hilfsfunktion für Zeitmessung
def current_time_ms():
    return utime.ticks_ms()

# Initialisiere den PID-Regler
pid = PIDControl(2.0, 0.0, 0.00, current_time_ms)

while True:
    set_point = adc_set_point.read_u16() / 65535 * 180  # Skalierung auf 0-180 Grad
    feedback = adc_feedback.read_u16() / 65535 * 180  # Skalierung auf 0-180 Grad
    
    pid.set_input(set_point - feedback)
    control_signal = pid.get_output()
    
    # Begrenzung des Signals auf den Servo-Bereich
    control_signal = max(min(control_signal, 180), 0)
    
    # Umrechnung in Duty Cycle für das Servo
    duty_cycle = int((control_signal + 30) * 65535 / 270)
    
    servo.duty_u16(duty_cycle)

    # Ausgaben für das Debugging
    print(f"Set Point: {set_point:.2f}, Feedback: {feedback:.2f}, Control Signal: {control_signal:.2f}, Duty Cycle: {duty_cycle}")

