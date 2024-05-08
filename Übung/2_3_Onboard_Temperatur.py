"""
MicroPython-Programm zur Darstellung des Onboard Temperatursensors
und normierte Ausgabe der Anzeige auf °C bzw. °F in der Konsole
Stand 26. Juli 2023 - Python 3.7 mit MicroPython Extension auf PyBoard (Pico)
"""
import machine
import time
adc = machine.ADC(4)
while True:
    ADC_spannung = adc.read_u16() * (3.3 / 65535)
    temp_in_celsius = 27 - (ADC_spannung - 0.706)/0.001721
    temp_in_fahrenheit = 32+(1.8*temp_in_celsius)
    print("On-Board Temperatur : {} °C {} °F".format(temp_in_celsius, temp_in_fahrenheit))
    time.sleep_ms(500)
