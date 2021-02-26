import os
import logging

import connexion
from flask_testing import TestCase

from openapi_server.encoder import JSONEncoder

from openapi_server.database import models


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.app.json_encoder = JSONEncoder
        app.add_api("openapi.yaml", pythonic_params=True)
        app.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
            "DATABASE_URL", "sqlite:///:memory:"
        )
        app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        models.db.init_app(app.app)
        return app.app

    def setUp(self):
        # check if db url envvar exists and add db to app
        # always seed the db if created
        models.db.create_all()

    def tearDown(self):
        models.db.session.remove()
        models.db.drop_all()
