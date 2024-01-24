def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
    print("Result:", result)
except ValueError as e:
    print("Error:", str(e))