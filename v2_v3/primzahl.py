def check_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    user_input = input("Bitte geben Sie eine positive ganze Zahl ein: ")

    number = int(user_input)
    if number <= 0:
        print("Bitte geben Sie eine positive ganze Zahl über 0 ein.")
        continue

    if check_prime(number):
        print(f"{number} ist eine Primzahl.")
    else:
        print(f"{number} ist keine Primzahl.")
