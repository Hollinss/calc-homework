"""Mod Calculation Class"""

# pylint: disable=too-few-public-methods

class Calculation:
    """calculation abstract base class"""
    def __init__(self,values: tuple):
        """constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)
    @staticmethod
    def convert_args_to_list_float(values):
        """convert list of arguments to floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
