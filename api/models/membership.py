# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import (
    Document,
    ObjectIdField,
    StringField,
    FloatField,
    DateField,
    EmbeddedDocument
)

membership_model = api.model('Memberships', {
    'customerId': fields.String(
        required=True,
        description='Information about the customer: CustomerId'
    ),
    'passMembership': fields.String(
        required=True,
        description='Type of the membership: Bronze:Silver:Gold'
    ),
    'price': fields.Float(
        required=True,
        description='Membership Price according to the pass'
    ),
    'startDate': fields.Date(
        required=True,
        description='Date when the membership was started'
    ),
    'endDate': fields.Date(
        required=True,
        description='Date when the membership was ended'
    )
})

# MongoDB Membership
class MembershipDocument(EmbeddedDocument):
    meta = {'collection': 'membership'}
    customer_id = ObjectIdField(required=True, unique=True)
    pass_membership = StringField(required=True, max_length=40)
    price = FloatField(required=True)
    start_date = DateField(required=True)
    end_date = DateField(required=True)

    def to_json(self):
        return {
            'customerId' : self.customer_id,
            'passMembership' : self.pass_membership,
            'price' : self.price,
            'startDate' : self.start_date,
            'endDate' : self.end_date
        }
