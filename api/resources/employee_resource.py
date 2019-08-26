# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARUs
import json
from flask import request
from flask_restplus import Resource
from api.models.employees import ns, employee_model, EmployeeDocument

@ns.route('')
class EmployeeList(Resource):
    """ Shows a list of all employees, lets you create a new employee """
    @ns.response(200, 'Success')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """ List all the employees from MongoDb """
        employees = []
        for employee in EmployeeDocument.objects():
            employees.append(json.loads(employee.to_json()))
        return {'employees': employees}, 200

    @ns.expect(employee_model)
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Creates employee in the db """
        try:
            payload = request.get_json(force=True)
            employee = EmployeeDocument(**payload).save()
            return json.loads(employee.to_json()), 200
        except Exception as error:
            return {'message': error}

@ns.route('/<employeeId>')
class Employee(Resource):
    """ Allows you to edit, delete, get specific employee """
    @ns.marshal_with(employee_model)
    @ns.response(200, 'Successs')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def get(self, employeeId):
        """ Specific employee is returned based on the id
                Args:
                    employeeId (str) : unique identifier
        """
        employee = EmployeeDocument.objects(id=employeeId)
        if employee:
            return json.loads(employee.to_json()), 200
        return {'message': 'Employee does not exist'}, 400

    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def delete(self, employeeId):
        """ Deletes the details of the employee based on the id
                Args:
                    employeeId (str) : unique identifier
        """
        employee = EmployeeDocument.objects(id=employeeId)
        if employee:
            employee.delete()
            return {'message' : 'Employee was deleted successful'}, 200
        return {'message' : 'Employee does not exist!'}, 400

    @ns.expect(employee_model)
    @ns.marshal_with(employee_model)
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def put(self, employeeId):
        """ Updates the details of the employee based on the id
                Args:
                    employeeId (str) : unique identifier
        """
        try:
            payload = request.get_json(force=True)
            employee = EmployeeDocument.objects(id=employeeId)
            if employee:
                employee.update_one(**payload)
                return json.loads(employee.to_json()), 200
        except Exception as error:
            raise ValueError(error)

