"""Multiplication test"""
from calc_mod.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """test multiplication"""
    mynumbers = (4.0,5.0,6.0)
    multiplication = Multiplication(mynumbers)
    assert multiplication.get_result() == 120.0
    