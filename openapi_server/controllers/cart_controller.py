import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server import util

from openapi_server.controllers import menu_controller
from openapi_server.database import CART


def add_cart_item():  # noqa: E501
    """Add a menu item a cart

    Creates a new item in the cart. Duplicates are allowed # noqa: E501

    :param menu_item: Item to add to the cart
    :type menu_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        menu_item = MenuItem.from_dict(connexion.request.get_json())  # noqa: E501
    # the spec is taking in the entire object, however that's technically not necessary
    CART.append(menu_item)


def delete_cart_item(item_id):  # noqa: E501
    """Remove item from cart

    The item must be in the cart. If multiple of same item, call this twice  # noqa: E501

    :param item_id: The menu item to delete from cart
    :type item_id: int

    :rtype: None
    """
    # this is by no means efficient
    for item in CART:
        if item.id == item_id:
            CART.remove(item)
            break
    else:
        return Error(403)  # cart is already devoid of this item


def list_cart(limit=None):  # noqa: E501
    """List all cart items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[MenuItem]
    """
    return CART
