"""
Ampelsqeuenz per Patternshift
"""
from rp2 import PIO, asm_pio, StateMachine
import time
from machine import Pin


@asm_pio(out_init=(PIO.OUT_LOW, PIO.OUT_LOW, PIO.OUT_HIGH))
def blink_pull():
    wrap_target()
    pull()
    set(x, 31)
    label("patternshift")
    set(y, 31)
# Bei jedem Schritt wird das Pattern um 4 Bit nach rechts geschoben
    out(pins, 4) [31]
    # delay
    label("inner_delay_loop")
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    jmp(y_dec, "inner_delay_loop")
    # delay ende
    jmp(x_dec, "patternshift")
    wrap()

sm = StateMachine(1, blink_pull, freq=2000, out_shiftdir=PIO.SHIFT_RIGHT, out_base=Pin(10))
sm.active(1)

adc = machine.ADC(4)
led = machine.Pin(25, machine.Pin.OUT)
zyklus = 0

while zyklus < 10:
# Die Phasen sind : Grün,Gelb,Rot,Rotgelb,Grün,Grün,Grün,Grün
# Bit 0 = Rot =  Pin 10
# Bit 1 = Gelb = Pin 11
# Bit 2 = Grün = Pin 12
# Bit 3 = unbenutzt
# Das 32-Bit Pattern wird nach rechts geschoben und deshalb bitweise von rechts nach links gelesen.
# ====== >>>>>>>> ======
# Binärformat
#    sm.put(0b01000100010001000011000100100100)
# Hexadezimalformat
     sm.put(0x44443124)
# Ausgabe der Onboard-Temperatur
    ADC_spannung = adc.read_u16() * (3.3 / 65535)
    temp_in_celsius = 27 - (ADC_spannung - 0.706)/0.001721
    temp_in_fahrenheit = 32+(1.8*temp_in_celsius)
    print("On-Board Temperatur : {} °C {} °F".format(temp_in_celsius, temp_in_fahrenheit))
# Blinken der Onboard-LED
    led(1)
    time.sleep_ms(500)
    led(0)
    print("Zyklus = ", zyklus)
    zyklus += 1
    time.sleep(1)
