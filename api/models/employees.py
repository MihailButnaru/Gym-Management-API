# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
from flask_restplus import fields
from api.routes import api
from mongoengine import (
    Document,
    StringField
)

employee_model = api.models('Employees', {
    'firstname': fields.String(
        required=True,
        description='Firstname of the employee'
    ),
    'lastname': fields.String(
        required=True,
        description='Lastname of the employee'
    ),
    'gender': fields.String(
        required=True,
        description='Gender M/F'
    ),
    'address': fields.String(
        required=True,
        description='Address of the employee'
    )
})

# MongoDB Schema
class Employee(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    gender = StringField(required=True, max_length=10)
    address = StringField(required=True, max_length=50)

    def to_json(self):
        return {
            'firstname': self.first_name,
            'lastname': self.last_name,
            'gender': self.gender,
            'address': self.address
        }