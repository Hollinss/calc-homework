"""Caclculation Abstract Class"""
class Calculation:

    #constructor
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB

    # base class of class hierarchy
    @classmethod
    def create(cls, valueA, valueB):
        return cls(valueA, valueB)