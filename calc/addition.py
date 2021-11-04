"""Addition class inherits from calcuation class"""

from calc.calculation import Calculation

class Addition(Calculation):
    """Gets result from calculation class"""
    def get_result(self):
        """Returns addition of two numbers"""
        return self.value_a + self.value_b
