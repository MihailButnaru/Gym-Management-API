# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import (
    Document,
    StringField,
    ListField,
    EmbeddedDocumentField
)

ns = api.namespace('employees', description='Employee Management operations.')

employee_model = api.model('Employees', {
    'firstname': fields.String(
        required=True,
        description='The firstname of the employee'
    ),
    'lastname': fields.String(
        required=True,
        description='The lastname of the employee'
    ),
    'dob': fields.String(
        required=True,
        description='Data of birth of the employee'
    ),
    'gender': fields.String(
        required=True,
        description='Employee gender [M/F]'
    ),
    'address': fields.String(
        required=True,
        description='The address of the employee'
    ),
    'postcode': fields.String(
        required=True,
        description='The postcode of the employee'
    ),
    'phoneNumber': fields.String(
        required=True,
        description='Mobile number of the employee'
    ),
    'email': fields.String(
        required=True,
        description='Email contact'
    )
})

# MongoDB Schema
class EmployeeDocument(Document):
    meta = {'collecation': 'employees'}
    firstname = StringField(required=True, max_length=15)
    lastname = StringField(required=True, max_length=15)
    dob = StringField(required=True, max_length=10)
    gender = StringField(required=True, max_length=15)
    address = StringField(required=True, max_length=120)
    postcode = StringField(required=True, max_length=15)
    phoneNumber = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)

    def to_json(self):
        models = {
            'id': str(self.id),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'dob': self.dob,
            'gender': self.gender,
            'address': self.address,
            'postcode': self.postcode,
            'phoneNumber': self.phoneNumber,
            'email': self.email
        }
        return json.dumps(models)