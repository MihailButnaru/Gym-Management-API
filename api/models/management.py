# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import fields
from api.routes.restplus import api
from mongoengine import Document, StringField, FloatField


ns = api.namespace('management', description='Management operations.')

management_model = api.model('Management', {
    'empName' : fields.String(
        required=True,
        description='Name of the employee'
    ),
    'position' : fields.String(
        required=True,
        description='Position of the management'
    ),
    'salary' : fields.Float(
        required=True,
        description='Salary'
    ),
    'seniority' : fields.String(
        required=True,
        description='Seniority of the employee'
    )
})

class ManagementDocument(Document):
    meta = {'collection':'management'}
    empName = StringField(required=True, max_length=25)
    position = StringField(required=True, max_length=50)
    salary = FloatField(required=True)
    seniority = StringField(required=True, max_length=50)

    def to_json(self):
        models = {
            'id' : str(self.id),
            'empName' : self.empName,
            'position' : self.position,
            'salary' : self.salary,
            'seniority' : self.seniority
        }
        return json.dumps(models)
