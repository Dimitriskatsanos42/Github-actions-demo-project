"""
calculator.py

A small, well-tested calculator module used as a demo project for
learning and showcasing GitHub Actions (CI/CD) with Python.
"""


def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b


def subtract_numbers(a, b):
    """Subtracts b from a and returns the result."""
    return a - b


def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b


def divide_numbers(a, b):
    """Divides a by b and returns the result.

    Raises:
        ValueError: if b is zero, since division by zero is undefined.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    a, b = 5, 10
    print(f"{a} + {b} = {add_numbers(a, b)}")
    print(f"{a} - {b} = {subtract_numbers(a, b)}")
    print(f"{a} * {b} = {multiply_numbers(a, b)}")
    print(f"{a} / {b} = {divide_numbers(a, b)}")
