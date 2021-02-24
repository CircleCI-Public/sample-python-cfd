#!/usr/bin/env python3
import os

import connexion

from openapi_server import encoder
from flask_cors import CORS
from openapi_server.database import models

app = connexion.App(__name__, specification_dir="./openapi/")
app.app.json_encoder = encoder.JSONEncoder
# app.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql:///test-cfd")
app.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqllite:///:memory:")  # can this work if there's no db to connect to?
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.add_api("openapi.yaml", arguments={"title": "CFD"}, pythonic_params=True)
CORS(app.app)
models.db.init_app(app.app)

def main():
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
