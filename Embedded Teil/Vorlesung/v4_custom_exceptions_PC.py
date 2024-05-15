from typing import Any, Dict, List

class ValidationError(Exception):
    def __init__(self, message: str, errors: List[str]):
        # Initialisiert die Exception mit einer Nachricht und speichert die individuellen Fehler.
        super().__init__(message)
        self.errors = errors  # Liste der spezifischen Fehlermeldungen.

def validate_user_input(data: Dict[str, Any]) -> str:
    """
    Überprüft, ob das gegebene Daten-Dictionary den Anforderungen entspricht.
    
    Args:
    data (Dict[str, Any]): Die zu validierenden Nutzerdaten.

    Returns:
    str: Eine Bestätigungsnachricht, dass die Eingabe gültig ist.

    Raises:
    ValidationError: Wenn die Eingabe nicht den Validierungsregeln entspricht.
    """
    errors = []  # Liste zur Speicherung von Fehlermeldungen.
    
    # Überprüfung, ob der Eingabetyp korrekt ist (muss ein Dictionary sein).
    if not isinstance(data, dict):
        errors.append("Input must be a dictionary.")
    
    # Überprüfung, ob der Name existiert und vom korrekten Typ ist.
    if "name" not in data or not isinstance(data["name"], str):
        errors.append("Name is required and must be a string.")
    
    # Überprüfung, ob das Alter existiert und in einem gültigen Bereich ist.
    if "age" not in data or not (isinstance(data["age"], int) and 0 <= data["age"] <= 120):
        errors.append("Age is required and must be an integer between 0 and 120.")
    
    # Wenn Fehler gefunden wurden, wird eine ValidationError ausgelöst.
    if errors:
        raise ValidationError("Invalid input data", errors)
    
    # Rückmeldung, dass keine Fehler gefunden wurden.
    return "Input is valid."

# Fehlerhafte Beispiel-Daten zum Testen der Funktion
faulty_user_input = {
    "name": 123,   # Fehler: Name sollte ein String sein
    "age": "dreißig"  # Fehler: Alter sollte eine Zahl sein
}

try:
    result = validate_user_input(faulty_user_input)
    print(result)
except ValidationError as e:
    print(f"An error occurred: {e}")
    print("Details:", e.errors)
