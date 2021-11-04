"""Division class inherits from calcuation class"""

from calc.calculation import Calculation

class Division(Calculation):
    """Gets result from calculation class"""
    def get_result(self):
        """Returns division"""
        if self.value_b == 0:
            raise Exception("Cannot divide by 0!")
        return self.value_a / self.value_b
