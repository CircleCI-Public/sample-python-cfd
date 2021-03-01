import os
import logging

import connexion
import pytest
from flask_testing import TestCase

from openapi_server.encoder import JSONEncoder

from openapi_server.database import models

def get_env(envvar: str, default=None):
    """Boolean envvars as strings suck, fix that"""
    var = os.getenv(envvar)
    if var and var.lower() in ("false", "0"):
        var = False
    elif var and var.lower() in ("true", "1"):
        var = True
    elif default:
        var = default
    return var

SKIP_DB_TESTS = get_env("SKIP_DB_TESTS", True)

class BaseTestCase(TestCase):
    def create_app(self):
        # no database is setup, any tests requiring a DB will fail and should use the "BaseDBTestCase"
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.app.json_encoder = JSONEncoder
        app.add_api("openapi.yaml", pythonic_params=True)
        return app.app

@pytest.mark.skipif(SKIP_DB_TESTS, reason="DB tests request skipping")
class BaseDBTestCase(BaseTestCase):

    def create_app(self):
        app = super().create_app()
        db_uri = os.getenv('DATABASE_URI', "")
        if "postgres" in db_uri:
            app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        else:
            raise RuntimeError("Request to run db tests, but postgresql db not connected")
        models.db.init_app(app)
        return app

    def setUp(self):
        # check if db url envvar exists and add db to app
        # always seed the db if created
        models.db.create_all()

    def tearDown(self):
        models.db.session.remove()
        models.db.drop_all()
