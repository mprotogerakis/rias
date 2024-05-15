import time
from machine import Pin
import rp2

# Definiert ein PIO-Programm (Programmable Input/Output) mit dem Namen blink_1hz
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    # Die gesamte Anzahl der Zyklen für den ersten Teil des Programms: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    # Der IRQ wird ausgelöst, indem eine relative Adresse von 0 angegeben wird.
    irq(rel(0))
    
    # Setzt den Pin auf High (1), um die LED einzuschalten.
    set(pins, 1)
    
    # Lädt den Wert 31 in das x-Register und wartet dann 5 zusätzliche Zyklen.
    set(x, 31)                  [5]
    
    # Bezeichnet den Start der Verzögerungsschleife für den High-Zustand.
    label("delay_high")
    
    # Wartet für 30 Zyklen (NOP = No Operation).
    nop()                       [29]
    
    # Verringert das x-Register und springt zurück zu "delay_high", wenn x nicht null ist.
    jmp(x_dec, "delay_high")

    # Die gesamte Anzahl der Zyklen für den zweiten Teil des Programms: 1 + 7 + 32 * (30 + 1) = 1000
    # Setzt den Pin auf Low (0), um die LED auszuschalten.
    set(pins, 0)
    
    # Lädt den Wert 31 in das x-Register und wartet dann 6 zusätzliche Zyklen.
    set(x, 31)                  [6]
    
    # Bezeichnet den Start der Verzögerungsschleife für den Low-Zustand.
    label("delay_low")
    
    # Wartet für 30 Zyklen (NOP = No Operation).
    nop()                       [29]
    
    # Verringert das x-Register und springt zurück zu "delay_low", wenn x nicht null ist.
    jmp(x_dec, "delay_low")

# Erstellt die StateMachine mit dem blink_1hz Programm und gibt die Signale auf Pin(25) aus.
sm = rp2.StateMachine(0, blink_1hz, freq=2000, set_base=Pin(25))

# Setzt den IRQ-Handler, um den Millisekunden-Zeitstempel auszugeben.
sm.irq(lambda p: print(time.ticks_ms()))

# Startet die StateMachine.
sm.active(1)