def berechne_fakultaet(n: int) -> int:
    fakultaet = 1
    i = 1
    while i <= n:
        fakultaet *= i
        i += 1
    return fakultaet

zahl = int(input("Bitte geben Sie eine Zahl ein: "))
ergebnis = berechne_fakultaet(zahl)
print(f"Die Fakultät von {zahl} ist: {ergebnis}")