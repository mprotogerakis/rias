from abc import ABC, abstractmethod


class PrimeCheckerInterface(ABC):
    @abstractmethod
    def check_prime(self, num: int) -> bool:
        pass


class PrimeChecker(PrimeCheckerInterface):
    def check_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


# Beispielverwendung
prime_checker = PrimeChecker()
print(prime_checker.check_prime(17))  # Ausgabe: True
print(prime_checker.check_prime(16))  # Ausgabe: False
