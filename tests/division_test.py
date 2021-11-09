"""testing division"""
from calc_mod.calculations.division import Division

def test_calculation_division():
    """test division"""
    mynumbers = (2.0,1.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5
