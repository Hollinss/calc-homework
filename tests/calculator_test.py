"""Testing the Calculator"""
from calculator.main import Calculator
import pprint
import pytest

@pytest.fixture
def clear_history():
    """Clearing the history [] before each test"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Addition Test"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2,2) == 4
    assert Calculator.get_result_of_latest_calculation_added() == 4
    assert Calculator.history_count() == 2
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    """Testing the clearing function of history []"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.clear_history() == True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    """Testing getting the count of history []"""
    assert Calculator.history_count() == 0
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.history_count() == 2

def test_get_last_calculation(clear_history):
    """Testing getting the last number from history []"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_result_of_latest_calculation_added() == 4

def test_get_first_calculation(clear_history):
    """Testing getting the first number from history []"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.get_first_calculation_from_history() == 3

def test_calculator_subtract(clear_history):
    """Testing Subtraction"""
    assert Calculator.subtract_number(5,2) == 3

def test_calculator_multiplication(clear_history):
    """Testing Multiplication"""
    assert Calculator.multiply_number(5,2) == 10

def test_calculator_division(clear_history):
    """Testing Division"""
    assert Calculator.divide_number(6,2) == 3
