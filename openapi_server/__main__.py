#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from flask_cors import CORS

app = connexion.App(__name__, specification_dir="./openapi/")
app.app.json_encoder = encoder.JSONEncoder
app.add_api("openapi.yaml", arguments={"title": "CFD"}, pythonic_params=True)
CORS(app.app)

def main():
    app.run(port=8080)


if __name__ == "__main__":
    main()
