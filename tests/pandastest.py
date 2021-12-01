"""Testing File for CSV Functionality"""
import pandas as pd
from calc_mod.calculations.addition import Addition
from tests.readcsv import Read
from tests.absolute import absolutepath

Read.readcsv( absolutepath('input_test_data/addition.csv') )

# file = pd.read_csv('input_test_data/addition.csv')

#file.to_csv('data2.csv', index = False)
# for index, row in file.iterrows():
#     mynumbers = (row['value_1'], row['value_2'])
#     print(mynumbers)
#
# df = pd.DataFrame(columns = ['value_1', 'value_2', 'result'])
# print("BEFORE:")
# print(df)
#
# for index, row in file.iterrows():
#     mynumbers = (row['value_1'], row['value_2'])
#     addition = Addition(mynumbers)
#     df = df.append( {'value_1' : row['value_1'],
#                     'value_2' : row['value_2']
#                    , 'result' : addition.get_result()},
#                    ignore_index = True )
#     #addition.get_result() == file.to_csv('data2.csv', index = False, )
#
# print("AFTER:")
# print(df)
# df.to_csv('output.csv', mode='a', index=False, header=False)