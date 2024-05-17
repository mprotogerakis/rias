FUNCTION_BLOCK st_1_DIY_BLINKER

// Deklaration der Eingangsvariablen
VAR_INPUT
    BlinkInterval : TIME := T#1S; // Blinkintervall, standardmäßig auf 1 Sekunde gesetzt
END_VAR

// Deklaration der Ausgangsvariablen
VAR_OUTPUT
    Q : BOOL := FALSE; // Ausgangsvariable, die den Zustand der LED repräsentiert, standardmäßig auf FALSE gesetzt
END_VAR

// Deklaration der internen Variablen
VAR
    BlinkTimer : TON; // TON-Timer (Einschaltverzögerung)
END_VAR

// Initialisierung des Timers
// Der Timer wird gestartet, wenn der Eingang IN wahr wird. 
// IN wird gesetzt auf NOT BlinkTimer.Q, d.h. der Timer startet erneut, wenn er abgelaufen ist.
// PT wird auf BlinkInterval gesetzt, was die Dauer des Timers bestimmt (1 Sekunde).
BlinkTimer(IN := NOT BlinkTimer.Q, PT := BlinkInterval);

// Logik für das Blinken der LED
// Wenn der Timer abgelaufen ist (Q des Timers ist TRUE),
// wird der Zustand der Ausgangsvariable Q umgekehrt (von TRUE auf FALSE oder von FALSE auf TRUE).
IF BlinkTimer.Q THEN
    Q := NOT Q; // LED-Zustand umkehren
END_IF
