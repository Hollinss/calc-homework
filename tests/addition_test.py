"""Testing the Addition Functionality"""
from calc_mod.calculations.addition import Addition

import pandas as pd


def test_calculation_addition():
    """testing addition"""
    # Arrange
    mynumbers = (1.0, 2.0, 30.5)
    # Act
    addition = Addition(mynumbers)
    # Assert
    assert addition.get_result() == result

    # -s for pytest to print out
    # read into dataframe
    # once you get dataframe to print, you can print to console
    # datamanager folder: reads and writes csv's

    # data_frame = pandas.read_csv(filename)
    # for row in data_frame
    # for key,value in row
    # result
    # list/tuple of the values that are the input for calculation

def test_calculation_addition_csv():
    """testing addition"""
    file = pd.read_csv('test_data/addition.csv')
    for index, row in file.iterrows():
        #Arrange
        mynumbers = (row['value_1'], row['value_2'])
        #Act
        addition = Addition(mynumbers)
        # Assert
        assert addition.get_result() == row['result']
