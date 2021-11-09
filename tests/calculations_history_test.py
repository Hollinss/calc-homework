"""Testing the calculator"""
import pytest
from calc_mod.history.calculations import Calculations
from calc_mod.calculations.multiplication import Multiplication

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture
def clear_history_fixture():
    """clear history each time"""
    Calculations.clear_history()
@pytest.fixture
def setup_multiplication_calculation_fixture():
    """define multiplication fixture"""
    values = (2,3)
    multiplication = Multiplication(values)
    Calculations.add_calculation(multiplication)

def test_adding_calculation_to_history(clear_history_fixture,setup_multiplication_calculation_fixture):
    """testing the count"""
    assert Calculations.count_history() == 1

def test_clear_calculation_history(clear_history_fixture,setup_multiplication_calculation_fixture):
    """testing the clear calculation functionality"""
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    assert Calculations.get_calculation(0).get_result() == 6

def test_get_calculation_last(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    assert Calculations.get_last_calculation().get_result() == 6

def test_get_calculation_first(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    assert Calculations.get_first_calculation().get_result() == 6


