import pandas as pd
from app.controllers.controller import BaseController
from calc_mod.calculator import Calculator
from calc_mod.history.calculations import Calculations
from tests.readcsv import Read
from flask import render_template, request, flash, redirect, url_for

class CalcController(BaseController):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            flash("Please enter a value")
        elif request.form['value1'] == '0' and request.form['operation'] == 'division':
            flash("Division by zero!")
        else:
            flash('Successful Calculation')

            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']

            my_tuple = (value1, value2)

            getattr(Calculator, operation)(my_tuple)
            result = str(Calculations.get_last_calculation_actual_value())
            Calculations.create_dataframe_to_write(value1, value2, result, operation)
            df = Read.csvreader()
            data = {
                'value1': [],
                'value2': [],
                'result': [],
                'operation': []
            }
            for index, row in df.iterrows():
                data["value1"].append(row['value_1'])
            #     # data["value2"].append(row['value_2'])
            #     # data["result"].append(row['result'])
            #     # data["operation"].append(row['operation performed'])

            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, data=data)
        return render_template('calculator1.html')
    @staticmethod
    def get():
        return render_template('calculator1.html')