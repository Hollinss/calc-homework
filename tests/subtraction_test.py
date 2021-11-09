"""Testing Subtraction Functionality"""
from calc_mod.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing subtraction"""
    mynumbers = (1.0,4.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == -5.0
