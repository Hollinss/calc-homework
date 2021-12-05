from app.controllers.controller import BaseController
from calc_mod.calculator import Calculator
from calc_mod.history.calculations import Calculations
from flask import render_template, request, flash, redirect, url_for

class CalcController(BaseController):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Please enter a value'
        else:
            flash('Successful Calculation')

            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']

            my_tuple = (value1, value2)

            getattr(Calculator, operation)(my_tuple)
            result = str(Calculations.get_last_calculation_actual_value())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator1.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator1.html')