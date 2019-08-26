# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from bson.objectid import ObjectId
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import EmbeddedDocument, StringField, IntField, DateTimeField, ObjectIdField

ns = api.namespace('classes', description='Classes Management operations.')

classes_model = api.model('Classes', {
    'className' : fields.String(
        required=True,
        description='Name of the class'
    ),
    'classTime' : fields.DateTime(
        required=True,
        description='Time when class starts'
    ),
    'maxAvailable' : fields.Integer(
        required=True,
        description='Number of people available to attend the class'
    )
})

class ClassDocument(EmbeddedDocument):
    meta = {'collection': 'classes'}
    _id = ObjectIdField(required=True, default=ObjectId)
    className = StringField(required=True, max_length=25)
    classTime = DateTimeField(required=True)
    maxAvailable = IntField(required=True)

    def to_json(self):
        models = {
            '_id' : str(self._id),
            'className' : self.className,
            'classTime' : self.classTime,
            'maxAvailable' : self.maxAvailable
        }
        return json.dumps(models)
