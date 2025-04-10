# Festgelegtes korrektes Passwort
korrektes_passwort = "geheim123"

# Solange fragen, bis das richtige Passwort eingegeben wird
while True:
    eingabe = input("Bitte geben Sie das Passwort ein: ")

    if eingabe == korrektes_passwort:
        print("Zugriff gewährt. Willkommen!")
        break
    else:
        print("Falsches Passwort. Bitte versuchen Sie es erneut.")