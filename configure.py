from openapi_server.__main__ import models, app


def create_db():
    app.app.app_context().push()
    models.db.drop_all()
    models.db.create_all()
    models.db.session.commit()


def seed_db():
    # db.session.add(item)
    # db.session.commit()
    pass


if __name__ == "__main__":
    create_db()
