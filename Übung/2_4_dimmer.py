"""
MicroPython-Programm zur Helligkeitssteuerung einer LED per Potentiometer
Stand 26. Juli 2023 - Python 3.7 mit MicroPython Extension auf PyBoard (Pico)
LED_1 an GPIO-Pin 10
Potentiometer an ADC-Kanal 2 (Pin 34)
"""
import machine
from machine import Pin, PWM
import time
sollwert = machine.ADC(2)
led1 = PWM(Pin(10))
led1.freq(1000)
while True:
    helligkeit = sollwert.read_u16()
    # Sollwert auf % ohne Nachkommastellen normieren
    print("Sollwert : {:.0f} %" .format(helligkeit * 100/65535))
    led1.freq(1000)
    led1.duty_u16(helligkeit)      # Einschaltdauer : 0-65535
    time.sleep_ms(50)
