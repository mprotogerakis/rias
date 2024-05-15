# Import necessary modules
from machine import Pin  # For GPIO pin control
from rp2 import PIO, StateMachine, asm_pio  # For using the PIO (Programmable Input/Output) features
from time import sleep  # For creating delays

# Define a PIO assembly program for PWM (Pulse Width Modulation)
@asm_pio(sideset_init=PIO.OUT_LOW)
def pwm_prog():
    pull(noblock) .side(0)  # Pull a word from TX FIFO to OSR without blocking and set side pin to 0
    mov(x, osr)  # Move the value from OSR to register X
    mov(y, isr)  # Move the value from ISR to register Y (preloaded with PWM count max)
    label("pwmloop")  # Define a loop label
    jmp(x_not_y, "skip")  # Jump to 'skip' if X is not equal to Y
    nop() .side(1)  # No operation and set side pin to 1 (generate PWM pulse)
    label("skip")  # Define a skip label
    jmp(y_dec, "pwmloop")  # Decrement Y and jump back to 'pwmloop' if Y is not zero

# Define a class to use the PIO program for PWM
class PIOPWM:
    def __init__(self, sm_id, pin, max_count, count_freq):
        # Initialize a state machine with the given parameters
        self._sm = StateMachine(sm_id, pwm_prog, freq=2 * count_freq, sideset_base=Pin(pin))
        
        # Load the max_count value into the ISR (Input Shift Register) of the state machine
        self._sm.put(max_count)  # Put max_count into the TX FIFO
        self._sm.exec("pull()")  # Execute 'pull()' to move value from TX FIFO to OSR
        self._sm.exec("mov(isr, osr)")  # Move the value from OSR to ISR
        
        # Activate the state machine
        self._sm.active(1)
        
        # Store the maximum count value
        self._max_count = max_count

    def set(self, value):
        # Ensure the value is within the range [-1, max_count]
        value = max(value, -1)  # Ensure the minimum value is -1 (completely turn off)
        value = min(value, self._max_count)  # Ensure the maximum value is max_count
        
        # Put the value into the TX FIFO of the state machine
        self._sm.put(value)

# Instantiate the PIOPWM class for pin 25 with specific parameters
pwm = PIOPWM(0, 25, max_count=(1 << 16) - 1, count_freq=10_000_000)

# Main loop to gradually fade the brightness of the LED
while True:
    for i in range(256):  # Loop from 0 to 255
        pwm.set(i ** 2)  # Set the PWM value (quadratic curve for smoother fading)
        sleep(0.01)  # Delay for 10 milliseconds