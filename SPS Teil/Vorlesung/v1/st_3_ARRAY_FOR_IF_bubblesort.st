PROGRAM st_3_ARRAY_FOR_IF_bubblesort
// Erstelle ein Programm bubblesort dass das gegebene Beispiel-Array sortiert
// Nutze den Debugger von Codesys um schrittweise das Array anzuzeigen.
VAR
	arr : ARRAY[1..10] OF INT := [34, 7, 23, 32, 5, 62, 23, 3, 1, 0]; // Beispiel-Array
    n : INT := 10;       // Größe des Arrays
    i, j : INT;          // Schleifenvariablen
    temp : INT;          // Temporäre Variable zum Vertauschen
    swapped : BOOL;      // Variable zum Überprüfen, ob Vertauschungen stattgefunden haben
END_VAR

// Bubble Sort Algorithmus
FOR i := 1 TO n - 1 DO
    swapped := FALSE;
    FOR j := 1 TO n - i DO
        IF arr[j] > arr[j + 1] THEN
            // Vertauschen der Elemente
            temp := arr[j];
            arr[j] := arr[j + 1];
            arr[j + 1] := temp;
            swapped := TRUE;
        END_IF
    END_FOR
    // Wenn keine Vertauschungen stattgefunden haben, ist das Array bereits sortiert
    IF NOT swapped THEN
        EXIT;
    END_IF
END_FOR

// Optional: Ausgabe des sortierten Arrays (abhängig von Ihrer Entwicklungsumgebung)
FOR i := 1 TO n DO
    // Print arr[i]; // Verwenden Sie eine geeignete Methode zur Ausgabe in Ihrer Umgebung
END_FOR