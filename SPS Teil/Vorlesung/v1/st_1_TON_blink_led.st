PROGRAM st_1_TON_blink_led
// Erstellen Sie ein ST-Programm in Codesys, das eine in der Webvisu von Codesys simulierte LED blinken lässt.

VAR
    LED : BOOL := FALSE;          // Variable zur Steuerung der LED, initial auf FALSE gesetzt
    BlinkTimer : TON;             // TON-Timer (Einschaltverzögerung)
    BlinkInterval : TIME := T#1s; // Blinkintervall, standardmäßig auf 1 Sekunde gesetzt
END_VAR

// Initialisierung des Timers
// Der Timer wird gestartet, wenn der Eingang IN auf TRUE gesetzt ist. 
// IN wird auf NOT BlinkTimer.Q gesetzt, sodass der Timer startet, wenn er abgelaufen ist (BlinkTimer.Q ist FALSE).
// PT wird auf BlinkInterval gesetzt, was die Dauer des Timers bestimmt (1 Sekunde).
BlinkTimer(IN := NOT BlinkTimer.Q, PT := BlinkInterval);

// Logik für das Blinken der LED
// Wenn der Timer abgelaufen ist (Q des Timers ist TRUE),
// wird der Zustand der LED (Variable LED) umgekehrt (von TRUE auf FALSE oder von FALSE auf TRUE).
IF BlinkTimer.Q THEN
    LED := NOT LED; // LED-Zustand umkehren
END_IF
