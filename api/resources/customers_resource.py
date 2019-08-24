# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
""" 
Customer Resource that allows you to add, edit, remove a customer
from the database.
"""
import json
from flask import request, jsonify, make_response
from flask_restplus import Resource
from api.models.customers import ns, customer_model, CustomerDocument

@ns.route('')
class CustomerList(Resource):
    """ Shows a list of all customers, lets you create a new customer """
    @ns.response(200, 'Success')
    def get(self):
        """ List all the customers from Mongodb """
        customers = []
        for customer in CustomerDocument.objects():
            customers.append(json.loads(customer.to_json()))
        return {'customers': customers}, 200

    @ns.expect(customer_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Create a customer in the database """
        try:
            payload = request.get_json(force=True)
            customer = CustomerDocument(**payload).save()
            return json.loads(customer.to_json()), 200
        except Exception as error:
            return {'message' : error}
