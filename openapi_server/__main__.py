#!/usr/bin/env python3
import logging
import os

import connexion

from openapi_server import encoder
from flask_cors import CORS
from openapi_server.database import models
from openapi_server.database import db_seed

app = connexion.App(__name__, specification_dir="./openapi/")
app.app.json_encoder = encoder.JSONEncoder
app.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///:memory:"
)  # connects to an in-memory db if no db url is available
app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.add_api("openapi.yaml", arguments={"title": "CFD"}, pythonic_params=True)
CORS(app.app)
models.db.init_app(app.app)

# Seed the database if we're running with an in memory-db
if "memory" in app.app.config.get("SQLALCHEMY_DATABASE_URI"):
    logging.warning("In memory db being used, please ensure a postgres DATABASE_URL is set")
    app.app.app_context().push()
    models.db.create_all()
    db_seed.seed()


def main():
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
