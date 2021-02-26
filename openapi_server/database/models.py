from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DataError


db = SQLAlchemy()

# helper method for easy mocking
def _commit_item(item):
    db.session.add(item)
    db.session.commit()


class MenuItem(db.Model):
    # definitely messes this up, the id should not be specified in the request
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.Float())
    # image_id = db.Column(db.Integer)   # this is probably broken
    image_id = db.Column(db.Integer, db.ForeignKey("image.id"))
    cart_id = db.Column(db.String, db.ForeignKey("cart.host"), nullable=True)

    def __init__(
        self,
        description,
        name,
        price,
        image_id,
        cart_id=None,
    ):
        self.description = description
        self.name = name
        self.price = price
        self.image_id = image_id  # this should probably be anohter reference to a model
        self.cart_id = cart_id

    def __repr__(self):
        return "<id {}>".format(self.id)

    # something like marshmallow would be a good addition if we were planning to scale this, but
    # there's just one model
    def serialize(self):
        return {
            "description": self.description,
            "id": self.id,
            "imageId": self.image_id,
            "name": self.name,
            "price": self.price,
        }

    @classmethod
    def add(cls, menu_item):
        item = cls(
            menu_item.description, menu_item.name, menu_item.price, menu_item.image_id
        )
        _commit_item(item)
        return item

    @classmethod
    def query_all(cls):
        return cls.query.all()

    @classmethod
    def query_by_id(cls, item_id):
        return cls.query.filter(MenuItem.id == item_id).first()


class Cart(db.Model):
    host = db.Column(db.String, primary_key=True)
    items = db.relationship("MenuItem")

    def __init__(self, host):
        self.host = host

    def __repr__(self):
        return "<host {}>".format(self.host)

    @classmethod
    def add_item(cls, host, menu_item):
        if len(Cart.query.filter(Cart.host == host).all()) < 1:
            new_cart = cls(host)
            db.session.add(new_cart)
        db_item = MenuItem.query.filter(MenuItem.id == menu_item.id).first()
        db_item.cart_id = host
        db.session.commit()

    @classmethod
    def query_by_host(cls, host):
        return cls.query.filter(Cart.host == host).first()

    @classmethod
    def delete_item_by_id(cls, host, item_id):
        cart = cls.query_by_host(host)
        for item in cart.items:
            if item.id == item_id:
                cart.items.remove(item)
                break
            db.session.commit()


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<id {}>".format(self.id)

    @classmethod
    def add(cls, raw_data):
        image = cls(raw_data)
        _commit_item(image)
        return image

    @classmethod
    def delete_image(cls, image_id):
        if not (image := cls.get_image(image_id)):
            raise DataError
        db.session.delete(image)
        db.session.commit()

    @classmethod
    def get_image(cls, image_id):
        return cls.query.filter(Image.id == image_id).first()
