# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Restplus provides information about the API
=> Must be initialized with a Flask Application
"""
import logging
from flask_restplus import Api

LOGGER = logging.getLogger(__name__)

api = Api(
    version='1.0',
    title='Gym Management Restful API',
    description='Gym Management API, allows you to manage all the services related to the gym.'
)

@api.errorhandler
def default_error_handler(error):
    """
    Registers a default error handler when an exception occured.
    """
    message = 'An unhandled exception occured.'
    LOGGER.exception(message)
    return {'message': '{}, {}'.format(message, error)}, 500
