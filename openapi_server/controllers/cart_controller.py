import connexion
import six
from sqlalchemy import exc
from sqlalchemy.sql.functions import mode

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server import util

from openapi_server.database import models
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def add_cart_item():  # noqa: E501
    """Add a menu item a cart

    Creates a new item in the cart. Duplicates are allowed # noqa: E501

    :param menu_item: Item to add to the cart
    :type menu_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        menu_item = MenuItem.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            models.Cart.add_item(connexion.request.remote_addr, menu_item)
            # models.Cart.add_item(connexion.request.host.split(':')[0], menu_item)
        except (SQLAlchemyError, TypeError, AttributeError):
            models.db.session.rollback()
            return Error(400), 400


def delete_cart_item(item_id):  # noqa: E501
    """Remove item from cart

    The item must be in the cart. If multiple of same item, call this twice  # noqa: E501

    :param item_id: The menu item to delete from cart
    :type item_id: int

    :rtype: None
    """
    # this is by no means efficient
    try:
        models.Cart.delete_item_by_id(connexion.request.remote_addr, item_id)
    except (SQLAlchemyError, TypeError):
        models.db.session.rollback()
        return Error(403), 403  # cart is already devoid of this item


def list_cart(limit=None):  # noqa: E501
    """List all cart items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[MenuItem]
    """
    if cart := models.Cart.query_by_host(connexion.request.remote_addr):
        return [_.serialize() for _ in cart.items]
    else:
        return []
