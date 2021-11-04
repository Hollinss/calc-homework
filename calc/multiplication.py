"""Multiplication class inherits from calcuation class"""

from calc.calculation import Calculation

class Multiplication(Calculation):
    """Gets result from calculation class"""
    def get_result(self):
        """Returns multiplication"""
        return self.value_a * self.value_b
