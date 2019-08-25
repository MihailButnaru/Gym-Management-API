# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Membership resource allows you to add, edit, remove a membership
that is linked to a specific customer.
"""
import json
from flask import request
from flask_restplus import Resource
from api.models.customers import CustomerDocument
from api.models.membership import ns, membership_model, MembershipDocument

@ns.route('/<customerId>')
class MembershipList(Resource):
    """ Shows a list of all memberships, lets you create a new membership"""
    @ns.response(200, 'Success')
    @ns.response(500, 'Internal Server Error')
    def get(self, customerId):
        """ List of all memberships, specific customer"""
        memberships = []
        document = CustomerDocument.objects(id=customerId)
        if document:
            for customer in document:
                for member_pass in customer.membership:
                    memberships.append(json.loads(member_pass.to_json()))
            return {'membership': memberships}, 200
        return {'message': 'Customer does not exist'}, 404

    @ns.expect(membership_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self, customerId):
        """ Create a new membership for the customer 
                Args:
                    customerId (str): unique identifier of the customer
        """
        try:
            payload = request.get_json(force=True)
            document = CustomerDocument.objects(id=customerId)
            if document:
                for customer in document:
                    membership = MembershipDocument(**payload)
                    customer.membership.append(membership)
                    customer.save()
                    return json.loads(membership.to_json()), 200
            return {'message': 'Customer does not exist!'}, 404
        except Exception as error:
            raise ValueError(error)

@ns.route('/<customerId>/pass/<membershipId>')
class Membership(Resource):
    """ Allows to edit, delete a membership """
    
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def delete(self, customerId, membershipId):
        """
        Deletes a specific membership based on the customerId
            Args:
                customerId (str): unique identifier of the customer
                membershipId (str): unique identifier of the membership
        """
        customers = CustomerDocument.objects(id=customerId)
        if customers:
            for customer in customers:
                for membership in customer.membership:
                    if str(membership._id) == membershipId:
                        CustomerDocument.objects.update(pull__membership___id=membershipId)
                        return {'message': 'Membership deleted'}, 200
                return {'message': 'Membership does not exist!'}, 404
        return {'message': 'Customer does not exist!'}, 404
                
    
    @ns.expect(membership_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def put(self, customerId, membershipId):
        """
        Updates a specific memberhsip based on the customerId
            Args:
                customerId (str): unique identifier of the customer
                memberhsipId (str): unique identifier of the membership
        """
        try:
            payload = request.get_json(force=True)
            customers = CustomerDocument.objects(id=customerId)
            if customers:
                for customer in customers:
                    for membership in customer.membership:
                        if str(membership._id) == membershipId:
                            pass
        except Exception as error:
            raise ValueError(error)
