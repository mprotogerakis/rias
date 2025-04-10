# Festgelegtes korrektes Passwort
korrektes_passwort = "geheim123"

# Maximale Anzahl an Versuchen
max_versuche = 3
versuch = 0

while versuch < max_versuche:
    eingabe = input("Bitte geben Sie das Passwort ein: ")
    versuch += 1

    if eingabe == korrektes_passwort:
        print("Zugriff gewährt. Willkommen!")
        break
    else:
        print(f"Falsches Passwort. Noch {max_versuche - versuch} Versuche übrig.")

if versuch == max_versuche and eingabe != korrektes_passwort:
    print("Zugriff verweigert. Zu viele Fehlversuche.")