# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Conftest used to import external plugins or modules
"""
import pytest
from mongoengine import connect, disconnect
from flask import Response as APIResponse, json
from flask.testing import FlaskClient
from werkzeug.utils import cached_property

from api.app import create_app
from api.config import Config

@pytest.fixture
def app():
    """ Set up global app for functional testing """
    class Response(APIResponse):
        @cached_property
        def json(self):
            return json.loads(self.data)

    class APIClient(FlaskClient):
        def open(self, *args, **kwargs):
            if 'json' in kwargs:
                kwargs['data'] = json.dumps(kwargs.pop('json'))
                kwargs['content_type'] = 'application/json'
            return super(APIClient, self).open(*args, **kwargs)

    _config = Config()
    app = create_app(_config)
    app.response_class = Response
    app.test_client_class = APIClient
    app.testing = True

    connect('mockDB', host='mongomock://localhost')  # MongoDB mock connection

    return app

@pytest.fixture
def client(app):
    return app.test_client()