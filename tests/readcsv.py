"""Function to read CSV"""
import pandas as pd
from writecsv import writecsv

class Read():
    def readcsv(filepath):
        file = pd.read_csv(filepath)
        return writecsv(file)