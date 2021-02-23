#!/usr/bin/env python3
import os

import connexion

from openapi_server import encoder
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir="./openapi/")
app.app.json_encoder = encoder.JSONEncoder
app.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.add_api("openapi.yaml", arguments={"title": "CFD"}, pythonic_params=True)
CORS(app.app)
db = SQLAlchemy(app)

def main():
    app.run(port=8000)


if __name__ == "__main__":
    main()
