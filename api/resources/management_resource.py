# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import Resource
from api.models.management import ns, ManagementDocument, management_model

@ns.route('')
class ManagementList(Resource):
    pass
