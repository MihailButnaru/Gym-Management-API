# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import logging
from api.routes.restplus import api
from api.resources.customers_resource import ns as customer_ns
from flask import Flask, Blueprint


def create_app(config):
    """ Flask Initialization application """
    logging.getLogger(__name__)

    # Flask
    app = Flask(__name__)

    # Swagger configuration
    app.config['SWAGGER_UI_DOC_EXPANSION'] = config.SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    app.config['RESTPLUS_ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP

    # Initialization
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(customer_ns)
    app.register_blueprint(blueprint)
    return app