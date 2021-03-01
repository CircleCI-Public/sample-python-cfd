import os
import logging

import connexion
import pytest
from flask_testing import TestCase
from openapi_server import database

from openapi_server.encoder import JSONEncoder

from openapi_server.database import models

DB_URI = os.getenv("DATABASE_URI", "")

class BaseTestCase(TestCase):
    def create_app(self):
        # no database is setup, any tests requiring a DB will fail and should use the "BaseDBTestCase"
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.app.json_encoder = JSONEncoder
        app.add_api("openapi.yaml", pythonic_params=True)
        return app.app


@pytest.mark.skipif("postgres" not in DB_URI, reason="No postgres database envvar, DB tests will skip")
class BaseDBTestCase(BaseTestCase):
    def create_app(self):
        app = super().create_app()
        if "postgres" in DB_URI:
            app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        else:
            raise RuntimeError(
                "Request to run db tests, but postgresql db not connected"
            )
        models.db.init_app(app)
        return app

    def setUp(self):
        models.db.create_all()

    def tearDown(self):
        models.db.session.remove()
        models.db.drop_all()
