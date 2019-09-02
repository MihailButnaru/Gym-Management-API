# Copyright | 2019
# All rights reserved
# MIHAIL BUTNARU
import json
from flask import request
from flask_restplus import Resource
from api.routes.restplus import api
from api.models.trainer import ns, TrainerDocument
from api.models.gym_classes import gym_class_model, GymClassDocument


@ns.route('/<trainerId>/gym')
class GymClassList(Resource):
    """ Shows a list of all gym classes, lets you create a new class """
    @ns.response(200, 'Success')
    @ns.response(500, 'Internal Server Error')
    def get(self, trainerId):
        """ List of all gym classes, specific trainer 
            Args:
                trainerId (objectId) : unique identifier of the trainer
        """
        gym_classes = []
        document = TrainerDocument.objects(id=trainerId)
        if document:
            for gym_class in document:
                for gym in gym_class.gymclass:
                    gym_classes.append(json.loads(gym.to_json()))
            return {'classes': gym_classes}, 200
        return {'message': 'Gym class does not exist'}, 400

    @ns.expect(gym_class_model)
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def post(self, trainerId):
        """ Create a gym class specific for the trainer 
            Args:
                trainerId (objectId) : unique identifier of the trainer
        """
        try:
            payload = request.get_json(force=True)
            document = TrainerDocument.objects(id=trainerId)
            if document:
                for trainer in document:
                    gym_class_document = GymClassDocument(**payload)
                    trainer.gymclass.append(gym_class_document)
                    trainer.save()
                    return json.loads(gym_class_document.to_json()), 200
            return {'message': 'Gym class does not exist!'}, 400
        except Exception as error:
            raise ValueError(error)


@ns.route('/<trainerId>/gym/<classId>')
class GymClass(Resource):
    """ Allows to edit, delete a gym class """
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def delete(self, trainerId, classId):
        """
        Deletes a specific gym class from a trainer
            Args:
                trainerId (objectId): unique identifier of the trainer
                classId (objectId): unique identifier of the gym class
        """
        trainers = TrainerDocument.objects(id=trainerId)
        if trainers:
            for trainer in trainers:
                for gym_class in trainer.gymclass:
                    if str(gym_class._id) == classId:
                        TrainerDocument.objects.update(pul__gymclass___id=classId)
                        return {'message' : 'Gym class was deleted!'}, 200
                return {'message' : 'Gym class does not exist!'}, 400
        return {'message' : 'Gym class does not exist!'}, 400

    @ns.expect(gym_class_model)
    @ns.response(200, 'Success')
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Internal Server Error')
    def put(self, trainerId, classId):
        """
        Updates a specific membership based on the trainerId
            Args:
                trainerId (objectId) : unique identifier of the trainer
                classId (objectId) : unique identifier of the gym class
        """
        try:
            payload = request.get_json(force=True)
            trainers = TrainerDocument.objects(id=trainerId)
            if trainers:
                for trainer in trainers:
                    for gym_class in trainer.gymclass:
                        if str(gym_class._id) == classId:
                            gym_class.className = payload['className']
                            gym_class.classTime = payload['classTime']
                            gym_class.maxAvailable = payload['maxAvailable']
                            trainer.save()
                            return payload, 200
        except Exception as error:
            raise ValueError(error)
