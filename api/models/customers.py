# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
"""
FlaskRest plus model and MongoDB Schema
is provided in order to create, edit and delete customers.
"""
import json
from flask_restplus import fields
from api.routes.restplus import api
from api.models.membership import MembershipDocument
from mongoengine import (
    Document,
    StringField,
    ListField,
    EmbeddedDocumentField
)

ns = api.namespace('customers', description='Customer Management operations.')

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
    'phoneNumber': fields.String(
        required=True,
        description='Mobile number of the customer'
    ),
    'email': fields.String(
        required=True,
        description='Email contact'
    )
})

# MongoDB Customer
class CustomerDocument(Document):
    meta = {'collection': 'customers'}
    firstname = StringField(required=True, max_length=15)
    lastname = StringField(required=True, max_length=15)
    dob = StringField(required=True, max_length=10)
    gender = StringField(required=True, max_length=15)
    address = StringField(required=True, max_length=120)
    postcode = StringField(required=True, max_length=15)
    phoneNumber = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)
    membership = ListField(EmbeddedDocumentField(MembershipDocument))

    def to_json(self):
        models = {
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