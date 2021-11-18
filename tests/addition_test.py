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

    #-s for pytest to print out
    #read into dataframe
    #once you get dataframe to print, you can print to console
    #datamanager folder: reads and writes csv's

    #data_frame = pandas.read_csv(filename)
    #for row in data_frame
        #for key,value in row
            #result
            #list/tuple of the values that are the input for calculation