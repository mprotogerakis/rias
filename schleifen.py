def calculate_sum(n: int) -> str:
    """
    Calculate the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range to sum up to.

    Returns:
        str: A formatted string representing the sum of numbers from 1 to n.
    """
    sum_of_numbers = sum(range(1, n + 1))
    result = f"Summe von 1 bis {n}: {sum_of_numbers}"
    return result

n = 100
final_result = calculate_sum(n)
print(final_result)