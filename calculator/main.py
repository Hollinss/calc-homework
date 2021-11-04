""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    #history array to hold values
    history = []
    @staticmethod
    def get_first_calculation_from_history():
        return Calculator.history[0].getResult()
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_latest_calculation_added():
        return Calculator.history[-1].getResult()
    @staticmethod
    def get_object_of_latest_calculation_added():
        return Calculator.history[-1]
    @staticmethod
    def add_number(valueA, valueB):
        """add number to result"""
        addition = Addition.create(valueA, valueB)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def subtract_number(valueA, valueB):
        """subtract numbers"""
        subtraction = Subtraction.create(valueA, valueB)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def multiply_number(valueA, valueB):
        """divide two numbers"""
        multiplication = Multiplication.create(valueA, valueB)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_latest_calculation_added()
    @staticmethod
    def divide_number(valueA,valueB):
        division = Division.create(valueA, valueB)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_latest_calculation_added()
