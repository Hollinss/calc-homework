"""This is the increment function"""
from calc_mod.calculations.addition import Addition
from calc_mod.calculations.subtraction import Subtraction
from calc_mod.calculations.multiplication import Multiplication
from calc_mod.calculations.division import Division
from calc_mod.calculations.calculation import Calculations

class Calculator:
    """This is the Calculator Class"""
    @staticmethod
    def add_numbers(*args):
        """adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_numbers(*args):
        """subtract list of numbers"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """multiplication numbers from result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def divide_numbers(*args):
        """divide numbers from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
