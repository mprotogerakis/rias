def calculate_sum(n: int) -> str:
    """
    Calculate the sum of numbers from 1 to a given integer 'n'.

    Args:
        n (int): The upper limit of the range to calculate the sum.

    Returns:
        str: A string containing the sum result in the format "Summe von 1 bis {n}: {sum_of_numbers}".
    """

    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    result = f"Summe von 1 bis {n}: {sum_of_numbers}"
    return result

n = 100
final_result = calculate_sum(n)
print(final_result)