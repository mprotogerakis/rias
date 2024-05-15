import time
import rp2
from machine import Pin

# Definiere das Blink-Programm. Es hat einen GPIO, der mit der Set-Anweisung verbunden wird, was ein Ausgangspin ist.
# Verwende viele Verzögerungen, um das Blinken mit dem Auge sichtbar zu machen.
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()       # Anfang der Schleife
    set(pins, 1)   [31] # Setze den Pin auf HIGH (LED an)
    nop()          [31] # Warte für eine bestimmte Zeit (31 Takte)
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31] # Setze den Pin auf LOW (LED aus)
    nop()          [31] # Warte für eine bestimmte Zeit (31 Takte)
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()             # Ende der Schleife

# Instanziiere eine Zustandsmaschine mit dem Blink-Programm, bei 2000Hz, mit Set verbunden zu Pin(25) (LED auf dem Pico-Board)
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))

# Starte die Zustandsmaschine für 3 Sekunden. Die LED sollte blinken.
sm.active(1)
time.sleep(3)
sm.active(0)