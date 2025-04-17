anzahl = int(input ("Wieviele Zahlen sollen erzeugt werden?"))

fibonacci_folge = [0, 1]

while len(fibonacci_folge) < anzahl:
    naechste_zahl = fibonacci_folge[-1] + fibonacci_folge[-2]
    fibonacci_folge.append(naechste_zahl)

print (f"Folge:{fibonacci_folge[:anzahl]}")


