class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Erstellen einer Instanz der Klasse Person
person1 = Person("John", 25)

# Aufrufen der Methode say_hello()
person1.say_hello()
