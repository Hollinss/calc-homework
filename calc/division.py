"""Division class inherits from calcuation class"""

from calc.calculation import Calculation

class Division(Calculation):
    """Gets result from calculation class"""
    def getResult(self):
        return self.valueA / self.valueB