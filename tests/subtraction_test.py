"""Testing Subtraction Functionality"""
from calc_mod.calculations.subtraction import Subtraction

import pandas as pd

def test_calculation_subtraction():
    """testing subtraction"""
    mynumbers = (1.0,4.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == 3.0

def test_calculation_subtraction_csv():
    """testing addition"""
    file = pd.read_csv('test_data/subtraction.csv')
    for index, row in file.iterrows():
        #Arrange
        mynumbers = (row['value_1'], row['value_2'])
        #Act
        subtraction = Subtraction(mynumbers)
        # Assert
        assert subtraction.get_result() == row['result']

