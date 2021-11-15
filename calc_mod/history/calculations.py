"""Calculations history class"""
from calc_mod.calculations.addition import Addition
from calc_mod.calculations.subtraction import Subtraction
from calc_mod.calculations.multiplication import Multiplication
from calc_mod.calculations.division import Division


class Calculations:
    """Class with fundamental methods to operate calculator"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """counts number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """gets latest calculation from user"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """gets first calculation from user"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """get a specific calculation from history input index"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(inserted_calculation):
        """append calculation from history"""
        return Calculations.history.append(inserted_calculation)

    @staticmethod
    def addition_calculation(values):  # pass list of values
        """add Addition to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Addition.create(values))
        return Calculations.history[-1]  # return the result of the addition from the history

    @staticmethod
    def multiplication_calculation(values):
        """add Multiplication to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.history[-1]

    @staticmethod
    def subtraction_calculation(values):
        """add Subtraction to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.history[-1]

    @staticmethod
    def division_calculation(values):
        """add Division to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Division.create(values))
        return Calculations.history[-1]
