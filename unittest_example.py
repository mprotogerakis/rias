from typing import List
import unittest

def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(limit: int) -> List[int]:
    """
    Return a list of prime numbers up to a specified limit.

    Args:
        limit (int): The upper limit for finding prime numbers.

    Returns:
        List[int]: A list of prime numbers up to the limit.
    """

    if limit <= 2:
        return []

    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

class TestGetPrimes(unittest.TestCase):

    def test_get_primes(self):
        self.assertEqual(get_primes(10), [2, 3, 5, 7])
        self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(get_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(get_primes(1), [])
        self.assertEqual(get_primes(2), [])

if __name__ == '__main__':
    unittest.main()