# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
import datetime
from bson.objectid import ObjectId
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import (
    Document,
    ObjectIdField,
    StringField,
    FloatField,
    DateTimeField,
    EmbeddedDocument
)
from api.utils.date_formatter import date_formatter

ns = api.namespace('membership', description='Membership Management operation.')

membership_model = api.model('Memberships', {
    'passMembership': fields.String(
        required=True,
        description='Type of the membership: Bronze:Silver:Gold'
    ),
    'price': fields.Float(
        required=True,
        description='Membership Price according to the pass'
    ),
    'startDate': fields.DateTime(
        default=datetime.datetime.utcnow(),
        required=True,
        description='Date when the membership was started'
    ),
    'endDate': fields.DateTime(
        required=True,
        description='Date when the membership was ended'
    )
})

# MongoDB Membership
class MembershipDocument(EmbeddedDocument):
    meta = {'collection': 'membership'}
    _id = ObjectIdField(required=True, default=ObjectId)
    passMembership = StringField(required=True, max_length=40)
    price = FloatField(required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)

    def to_json(self):
        models = {
            '_id': str(self._id),
            'passMembership' : self.passMembership,
            'price' : self.price,
            'startDate' : date_formatter(self.startDate),
            'endDate' : date_formatter(self.endDate)
        }
        return json.dumps(models)
