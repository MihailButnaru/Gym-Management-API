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
    passMembership = StringField(required=True, max_length=40)
    price = FloatField(required=True)
    startDate = DateField(required=True)
    endDate = DateField(required=True)

    def to_json(self):
        models = {
            'passMembership' : self.passMembership,
            'price' : self.price,
            'startDate' : self.startDate,
            'endDate' : self.endDate
        }
        return json.dumps(models)
