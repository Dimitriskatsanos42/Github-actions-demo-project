"""
test_calculator.py

Unit tests for calculator.py, run automatically by the CI workflow
on every push and pull request.
"""

import pytest
from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)


def test_add_positive_numbers():
    assert add_numbers(5, 10) == 15


def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5


def test_add_zero():
    assert add_numbers(0, 0) == 0


def test_subtract_numbers():
    assert subtract_numbers(10, 4) == 6


def test_subtract_results_in_negative():
    assert subtract_numbers(4, 10) == -6


def test_multiply_numbers():
    assert multiply_numbers(3, 7) == 21


def test_multiply_by_zero():
    assert multiply_numbers(100, 0) == 0


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
