# Anzahl der Fibonacci-Zahlen vom Benutzer abfragen und in eine Ganzzahl umwandeln
anzahl = int(input("Wie viele Fibonacci-Zahlen sollen erzeugt werden? "))

# Startwerte der Fibonacci-Folge: 0 und 1
fibonacci_folge = [0, 1]

# Solange die Liste kürzer ist als die gewünschte Anzahl ...
while len(fibonacci_folge) < anzahl:
    # ... berechne die nächste Zahl (Summe der letzten beiden Zahlen)
    naechste_zahl = fibonacci_folge[-1] + fibonacci_folge[-2]
    # Füge die neue Zahl zur Liste hinzu
    fibonacci_folge.append(naechste_zahl)

# Gib die Fibonacci-Folge aus (genau so viele Zahlen wie gewünscht)
print("Fibonacci-Folge:")

# Die folgende Zeile gibt die ersten 'anzahl' Elemente der Liste aus:
# - [:anzahl] ist ein sogenannter "Slicing"-Operator
# - Er schneidet die Liste so zu, dass nur die ersten 'anzahl' Einträge enthalten sind
# - Beispiel: wenn die Liste [0, 1, 1, 2, 3, 5, 8] ist und anzahl = 5,
#   dann wird [0, 1, 1, 2, 3] ausgegeben
print(fibonacci_folge[:anzahl])
#print(fibonacci_folge)