"""Testing the Addition Functionality"""
from calc_mod.calculations.addition import Addition

def test_calculation_addition():
    """testing addition"""
    #Arrange
    mynumbers = (1.0,2.0,30.5)
    #Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 33.5