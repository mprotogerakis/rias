def calculate_sum(n):
    sum_of_number = 0
    for i in range(1, n + 1):
        sum_of_number = sum_of_number + i
    return sum_of_number


def calculate_sum2(n):
    return sum(range(1, n + 1))


print(calculate_sum2(10))
