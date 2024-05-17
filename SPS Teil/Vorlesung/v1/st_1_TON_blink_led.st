PROGRAM st_1_TON_blink_led
// Erstellen Sie ein ST-Programm in Codesys dass eine in der Webvisu von Codesys simulierte LED blinken läasst.
VAR
	LED : BOOL := FALSE;          // Variable zur Steuerung der LED
    BlinkTimer : TON;             // Einschaltverzögerung (Timer On)
    BlinkInterval : TIME := T#1s; // Blinkintervall (1 Sekunde)
END_VAR

// Initialisierung des Timers
BlinkTimer(IN := NOT BlinkTimer.Q, PT := BlinkInterval);

// Logik für das Blinken der LED
IF BlinkTimer.Q THEN
    LED := NOT LED; // LED-Zustand umkehren
END_IF