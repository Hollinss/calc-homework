"""Testing the Calculator"""
import pytest
from calc_mod.calculator import Calculator
from calc_mod.history.calculations import Calculations

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture
def clear_history_fixture():
    """Clearing the history [] before each test"""
    Calculations.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """Addition Test"""
    assert Calculator.add_numbers(1.0,1.0,3.0) == 5.0

def test_calculator_subtract_static(clear_history_fixture):
    """Subtraction Static Test"""
    assert Calculator.subtract_numbers(19.0, 5.0, 4.0) == -28.0

def test_calculator_multiply_static(clear_history_fixture):
    """Multiplication Static Test"""
    assert Calculator.multiply_numbers(20.0,1.0,5.0) == 100.0

def test_calculator_divide_static(clear_history_fixture):
    """Divide Static Test"""
    assert Calculator.divide_numbers(5.0,50.0) == 10.0
