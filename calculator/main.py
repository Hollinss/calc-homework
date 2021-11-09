""" This is the increment function"""
from calc_mod.calculations.addition import Addition
from calc_mod.calculations.subtraction import Subtraction
from calc_mod.calculations.multiplication import Multiplication
from calc_mod.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    #history array to hold values
    history = []
    @staticmethod
    def get_first_calculation_from_history():
        """Returns first calculation from history"""
        return Calculator.history[0].get_result()
    @staticmethod
    def clear_history():
        """Clears history[]"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """Returns length of history"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """adds values to history"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_latest_calculation_added():
        """Returns last calculation result from history"""
        return Calculator.history[-1].get_result()
    @staticmethod
    def get_object_of_latest_calculation_added():
        """Returns latest calculation class from history"""
        return Calculator.history[-1]
    @staticmethod
    def add_number(value_a, value_b):
        """add number to result"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def subtract_number(value_a, value_b):
        """subtract numbers"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def multiply_number(value_a, value_b):
        """multiply two numbers"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def divide_number(value_a,value_b):
        """divide two numbers"""
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_latest_calculation_added()
