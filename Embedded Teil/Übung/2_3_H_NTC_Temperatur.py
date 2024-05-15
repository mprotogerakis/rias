"""
MicroPython-Programm zur Messwertumformung eines NTC-Temperatursensors
und normierten Ausgabe der Anzeige auf °C bzw. °F in der Konsole
Stand 15. April 2024 - Python 3.7 mit MicroPython Extension auf Raspberry Pi Pico (RP2040)
"""
import machine
import math
import time
BETA = 3950
R1 = 10000
V_REF = 3.3

adc = machine.ADC(2)
while True:
    ADC_spannung = adc.read_u16() * (V_REF / 65535)
    Widerstand = R1 / ((V_REF / ADC_spannung)-1)
    temp_in_Kelvin = 1 / (1 / 298.15 + 1 / BETA * math.log(Widerstand / 10000))
    temp_in_celsius = temp_in_Kelvin - 273.15
    temp_in_fahrenheit = 32+(1.8*temp_in_celsius)
    print("NTC-Temperatur : {} °C {} °F".format(temp_in_celsius, temp_in_fahrenheit))
    time.sleep_ms(500)
