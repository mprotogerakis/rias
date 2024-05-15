# Beispiel mit Call by Value

def increment_value(x: int):
    x += 1

value = 10
increment_value(value)
print("Wert nach Call by Value:", value)  # Ausgabe: 10


# Beispiel mit Call by Reference

class Data:
    def __init__(self, value: int):
        self.value = value

def increment_reference(data: Data):
    data.value += 1

data_obj = Data(10)
increment_reference(data_obj)
print("Wert nach Call by Reference:", data_obj.value)  # Ausgabe: 11