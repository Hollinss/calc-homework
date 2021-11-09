""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    #history array to hold values
    history = []
    @staticmethod
    def get_first_calculation_from_history():
        """Returns first calculation from history"""
        return Calculator.history[0].get_result()
    @staticmethod
    def clear_history():
        """Clears history[]"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """Returns length of history"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """adds values to history"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_latest_calculation_added():
        """Returns last calculation result from history"""
        return Calculator.history[-1].get_result()
    @staticmethod
    def get_object_of_latest_calculation_added():
        """Returns latest calculation class from history"""
        return Calculator.history[-1]
