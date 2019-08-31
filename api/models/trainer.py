# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import (
    Document,
    StringField,
    FloatField
)

ns = api.namespace('trainers', description='Trainers Management operation.')

trainer_model = api.model('Trainers', {
    'position' : fields.String(
        required=True,
        description='Position level of the trainer'
    ),
    'salary' : fields.Float(
        required=True,
        description='Salary of the trainer'
    ),
    'seniority' : fields.String(
        required=True,
        description='Seniority of the trainer'
    )
})

# MongoDB Trainer
class TrainerDocument(Document):
    meta = {'collection' : 'trainers'}
    position = StringField(required=True, max_length=25)
    salary = FloatField(required=True)
    seniority = StringField(required=True, max_length=25)

    def to_json(self):
        models = {
            'id' : str(self.id),
            'position' : self.position,
            'salary' : self.salary,
            'seniority' : self.seniority
        }
        return json.dumps(models)