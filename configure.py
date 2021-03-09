import argparse

from openapi_server.__main__ import models, app
from openapi_server.database import db_seed



def create_db():
    app.app.app_context().push()
    models.db.drop_all()
    models.db.create_all()
    models.db.session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', action='store_true', default=False)
    args = parser.parse_args()
    create_db()
    if args.seed:
        db_seed()
