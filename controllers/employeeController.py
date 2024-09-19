from flask import request, jsonify

# from application.caching import create_cache
from schemas import employee_schema, employees_schema
import services.employeeServices as employeeService
from marshmallow import ValidationError
from application.caching import cache

def save():
    try:
        employee_data = employee_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 422

    employee_save = employeeService.save(employee_data)
    if employee_save is not None:
        return employee_schema.jsonify(employee_save), 201
    else:
        return jsonify({'message': 'Error to save data.'}), 400

def find_all():
    employees = employeeService.find_all()
    return employees_schema.jsonify(employees), 200