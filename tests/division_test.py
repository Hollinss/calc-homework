"""testing division"""
import pytest

from calc_mod.calculations.division import Division

import pandas as pd


def test_calculation_division():
    """test division"""
    mynumbers = (2.0, 1.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5


# test for division by zero
def test_division_by_zero():
    """test division by zero"""
    mynumbers = (0.0, 2.0)
    Division(mynumbers)
    assert pytest.raises(ZeroDivisionError)

def test_calculation_division_csv():
    """testing multiplication from imported csv"""
    file = pd.read_csv('test_data/division.csv')
    for index, row in file.iterrows():
        #Arrange
        mynumbers = (row['value_1'], row['value_2'])
        #Act
        division = Division(mynumbers)
        # Assert
        assert division.get_result() == row['result']
