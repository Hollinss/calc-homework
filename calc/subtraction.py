"""Subtraction class inherits from calcuation class"""

from calc.calculation import Calculation

class Subtraction(Calculation):
    """Gets result from calculation class"""
    def get_result(self):
        """Returns subtraction"""
        return self.value_a - self.value_b
