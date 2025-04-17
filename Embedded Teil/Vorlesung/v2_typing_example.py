from typing import List


def double_numbers(numbers: List[int]) -> List[int]:
    doubled = [num * 2 for num in numbers]
    return doubled


result = double_numbers([1, 2, 3])
print(result)
