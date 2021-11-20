"""Multiplication test"""
from calc_mod.calculations.multiplication import Multiplication

import pandas as pd

def test_calculation_multiplication():
    """test multiplication"""
    mynumbers = (4.0,5.0,6.0)
    multiplication = Multiplication(mynumbers)
    assert multiplication.get_result() == 120.0

def test_calculation_multiplication_csv():
    """testing multiplication from imported csv"""
    file = pd.read_csv('test_data/multiplication.csv')
    for index, row in file.iterrows():
        #Arrange
        mynumbers = (row['value_1'], row['value_2'])
        #Act
        multiplication = Multiplication(mynumbers)
        # Assert
        assert multiplication.get_result() == row['result']
