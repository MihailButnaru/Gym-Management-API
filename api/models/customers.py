# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import fields
from api.routes import api
from mongoengine import (
    Document,
    StringField
)

customer_model = api.model('Customers', {
    'firstname': fields.String(
        required=True,
        description='The firstname of the customer'
    ),
    'lastname': fields.String(
        required=True,
        description='The lastname of the customer'
    ),
    'dob': fields.String(
        required=True,
        description='Data of birth of the customer'
    ),
    'gender': fields.String(
        required=True,
        description='Customer gender [M/F]'
    ),
    'address': fields.String(
        required=True,
        description='The address of the customer'
    ),
    'postcode': fields.String(
        required=True,
        description='The postcode of the customer'
    ),
    'mobilePhone': fields.String(
        required=True,
        description='Mobile number of the customer'
    ),
    'email': fields.String(
        required=True,
        description='Email contact'
    )
})

# MongoDB Schema
class Customer(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    dob = StringField(required=True, max_length=50)
    gender = StringField(required=True, max_length=50)
    address = StringField(required=True, max_length=120)
    postcode = StringField(required=True, max_length=50)
    mobile_phone = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)

    def to_json(self):
        return {
            'firstname': self.first_name,
            'lastname': self.last_name,
            'dob': self.dob,
            'gender': self.gender,
            'address': self.address,
            'postcode': self.postcode,
            'phone': self.mobile_phone,
            'email': self.email
        }