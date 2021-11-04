"""Caclculation Abstract Class"""
class Calculation:
    """Caclculation Abstract Class Definition"""

    #constructor
    def __init__(self, value_a, value_b):
        """Instantiate values a and b"""
        self.value_a = value_a
        self.value_b = value_b

    # base class of class hierarchy -> Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """Create a calculation object with two values"""
        return cls(value_a, value_b)
