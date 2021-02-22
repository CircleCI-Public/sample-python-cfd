from openapi_server.__main__ import db
from sqlalchemy.dialects import postgresql

# MenuItems are a one to many relationship between the Cart
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.Float())
    image_id = db.Column(db.Integer)   # this is probably broken
    # image_id = db.Column(db.Integer, ForeignKey('image.id'))
    # image = relationship("Image", back_populates="menuItem")
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.host'), nullable=False)

    def __init__(
        self, description, name, price, image_id, menu_name,
    ):
        self.description = description
        self.name = name
        self.price = price
        self.image_id = image_id  # this should probably be anohter reference to a model
        self.menu_name = menu_name

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Cart(db.Model):
    host = db.Column(postgresql.INET, primary_key=True)
    items = db.relationship('MenuItem')

    def __init__(
        self, host, items,
    ):
        self.host = host
        self.items = items

    def __repr__(self):
        return '<name {}>'.format(self.name)

class Images:
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)


    def __init__(
        self, data,
    ):
        self.data = data