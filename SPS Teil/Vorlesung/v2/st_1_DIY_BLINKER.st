FUNCTION_BLOCK st_1_DIY_BLINKER
VAR_INPUT
	BlinkInterval : TIME := T#1S; // Blinkintervall (1 Sekunde)
END_VAR
VAR_OUTPUT
	Q : BOOL := FALSE;   
END_VAR
VAR
    BlinkTimer : TON;             // Einschaltverzögerung (Timer On)
END_VAR

// Initialisierung des Timers
BlinkTimer(IN := NOT BlinkTimer.Q, PT := BlinkInterval);

// Logik für das Blinken der LED
IF BlinkTimer.Q THEN
    Q := NOT Q; // LED-Zustand umkehren
END_IF