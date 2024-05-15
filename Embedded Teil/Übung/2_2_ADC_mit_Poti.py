"""
MicroPython-Programm zur Spannungsmessung an einem Potentiometer
Stand 26. Juli 2023 - Python 3.7 mit MicroPython Extension auf PyBoard (Pico)
Pinbelegung :
Poti-Pin 1 an A-GND (Pin 33)
Poti-Pin 3 an 3V3_O (Pin 36)
Poti-Pin 2 an ADC-V (Pin 34) Kanal 2
"""

# Im Terminal werden Digitalwert und entsprechende Spannung angezeigt
#
from machine import ADC
import time
adc = ADC(2)
while True:
    digital_value = adc.read_u16()
    print("ADC-Wert =", digital_value)
    # Normierung auf Spannungswert
    voltage_value = 3.3*(digital_value/65535)
    winkel = 270 * (digital_value/65535)
    print("Spannung am Poti : {} V ".format(voltage_value))
    print("Drehwinkel des Poti : {} °".format(winkel))
    time.sleep_ms(500)
