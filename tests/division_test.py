"""testing division"""
import pytest

from calc_mod.calculations.division import Division

def test_calculation_division():
    """test division"""
    mynumbers = (2.0,1.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5

#test for division by zero
def test_divisio_by_zero():
    """test division by zero"""
    mynumbers = (0.0, 2.0)
    division = Division(mynumbers)
    with pytest.raises(ZeroDivisionError):
        assert division.get_result() == 0.0