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
    'address': fields.String(
        required=True,
        description='The address of the customer'
    ),
    'postcode': fields.String(
        required=True,
        description='The postcode of the customer'
    ),
    'genre': fields.String(
        required=True,
        description='Customer genre [M/F]'
    )
})

# MongoDB Schema
class Customer(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    address = StringField(required=True, max_length=120)
    postcode = StringField(required=True, max_length=50)
    genre = StringField(required=True, max_length=50)

    def to_json(self):
        return {
            'firstname': self.first_name,
            'lastname': self.last_name,
            'address': self.address,
            'postcode': self.postcode,
            'genre': self.genre
        }