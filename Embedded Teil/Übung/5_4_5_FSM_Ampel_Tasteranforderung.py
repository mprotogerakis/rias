"""
Ampelsqeuenz per Patternshift
SM1 steuert Ampelzyklus
SM0 fragt Button 1 ab -> Interrupt -> Schieberegister mit Pattern laden -> SM1
ToDo : Entprellung, Grünphase nach SM1-Zyklus halten
"""
from rp2 import PIO, asm_pio, StateMachine
import time
from machine import Pin

@rp2.asm_pio(out_init=(PIO.OUT_LOW, PIO.OUT_LOW, PIO.OUT_HIGH))
def blink_pull():
    wrap_target()
    pull()
    set(x, 10)
    label("patternshift")
    set(y, 10)
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


# Tasterüberwachung mit SM
@rp2.asm_pio()
def wait_pin_low():
    wrap_target()
    wait(0, pin, 0)
    irq(block, rel(0))
    wait(1, pin, 0)
    wrap()

def handler(sm):
    #Hier wird das Schieberegister für den Fußgängerzyklus geladen.
    # SM1 laden
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
    sm1.put(0x44443124)
    # DEBUG
    #print("INT")
    #

# Instanziierung Statemachine 0 : Tasterüberwachung
pin20 = Pin(20, Pin.IN)
sm0 = rp2.StateMachine(0, wait_pin_low, in_base=pin20)
sm0.active(1)
sm0.irq(handler)

# Instanziierung Statamachine 1 : Fußgängerzyklus
sm1 = rp2.StateMachine(1, blink_pull, freq=2000, out_shiftdir=PIO.SHIFT_RIGHT, out_base=Pin(10))
sm1.active(1)

# Haupt-CPU
# Onboard-Temperatursensor + Onbaord-LED
adc = machine.ADC(4)
led = machine.Pin(25, machine.Pin.OUT)
zyklus = 0

# Ausgabeschleife
while zyklus < 10:
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
