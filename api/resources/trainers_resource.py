# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
from flask_restplus import Resource
from flask import request
from api.routes.restplus import api
from api.models.trainer import ns, TrainerDocument, trainer_model

@ns.route('')
class TrainersList(Resource):
    """ Shows a list of trainers """
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """ Returns a list of trainers """
        trainers = []
        for trainer in TrainerDocument.objects():
            trainers.append(json.loads(trainer.to_json()))
        return {'trainers': trainers}, 200

    @ns.expect(trainer_model)
    @ns.response(201, 'Created')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Creates a new trainer """
        try:
            payload = request.get_json(force=True)
            trainer = TrainerDocument(**payload).save()
            return json.loads(trainer.to_json()), 201
        except Exception as error:
            return {'message': error}

@ns.route('/<trainerId>')
class Trainers(Resource):
    """ Allows you to edit, delete and get a specific trainer """
    @ns.marshal_with(trainer_model, code=200)
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def get(self, trainerId):
        """
        Baded on the trainerId, details of the trainer is returned
            Args:
                trainerId (str) : unique id of the trainer
        """
        if TrainerDocument.objects(id=trainerId):
            return json.loads(TrainerDocument.objects(id=trainerId).to_json()), 200
        raise Exception('Trainer does not exist!')

    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def delete(self, trainerId):
        """
        Based on the trainerId, a trainer is deleted
            Args:
                trainerId (str) : unique id of the trainer
        """
        if TrainerDocument.objects(id=trainerId):
            TrainerDocument.objects(id=trainerId).delete()
            return {'message' : 'Trainer was deleted successful'}, 200
        raise Exception('Trainer with this id does not exist')

    @ns.expect(trainer_model)
    @ns.marshal_with(trainer_model, code=200)
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def put(self, trainerId):
        """
        Based on the trainerId, details of the trainer are edited
            Args:
                trainerId (str) : unique id of the trainer
        """
        try:
            payload = request.get_json(force=True)
            trainer = TrainerDocument.objects(id=trainerId)
            if trainer:
                trainer.update_one(**payload)
                return json.loads(trainer.to_json()), 200
        except Exception as error:
            return {'message' : error}


