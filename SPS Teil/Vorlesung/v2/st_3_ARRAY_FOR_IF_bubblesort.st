PROGRAM st_3_ARRAY_FOR_IF_bubblesort
// Erstelle ein Programm bubblesort, das das gegebene Beispiel-Array sortiert
// Nutze den Debugger von Codesys, um schrittweise das Array anzuzeigen.

VAR
    arr : ARRAY[1..10] OF INT := [34, 7, 23, 32, 5, 62, 23, 3, 1, 0]; // Beispiel-Array mit 10 Integer-Werten
    n : INT := 10;       // Größe des Arrays, hier auf 10 gesetzt
    i, j : INT;          // Schleifenvariablen zur Iteration durch das Array
    temp : INT;          // Temporäre Variable zum Vertauschen von Elementen
    swapped : BOOL;      // Variable zum Überprüfen, ob Vertauschungen stattgefunden haben
END_VAR

// Bubble Sort Algorithmus
// Äußere Schleife: Wiederholt den Sortiervorgang n-1 mal
FOR i := 1 TO n - 1 DO
    swapped := FALSE;  // Zu Beginn jeder Iteration wird swapped auf FALSE gesetzt
    // Innere Schleife: Geht durch das Array und vergleicht benachbarte Elemente
    FOR j := 1 TO n - i DO
        // Wenn das aktuelle Element größer ist als das nächste, werden sie vertauscht
        IF arr[j] > arr[j + 1] THEN
            // Vertauschen der Elemente
            temp := arr[j];         // Temporärspeicher für arr[j]
            arr[j] := arr[j + 1];   // Setze arr[j] auf arr[j + 1]
            arr[j + 1] := temp;     // Setze arr[j + 1] auf den Wert von arr[j]
            swapped := TRUE;        // Markiere, dass eine Vertauschung stattgefunden hat
        END_IF
    END_FOR
    // Wenn in einer gesamten Durchgang keine Vertauschung stattgefunden hat, ist das Array sortiert
    IF NOT swapped THEN
        EXIT;  // Beendet die äußere Schleife vorzeitig
    END_IF
END_FOR

// Optional: Ausgabe des sortierten Arrays (abhängig von Ihrer Entwicklungsumgebung)
// Diese Schleife kann genutzt werden, um das sortierte Array zu überprüfen
FOR i := 1 TO n DO
    // Print arr[i]; // Verwenden Sie eine geeignete Methode zur Ausgabe in Ihrer Umgebung
    // Beispiel: Writen Sie in einer Codesys-Umgebung die Werte in das Log
    // Trace(arr[i]);
END_FOR
