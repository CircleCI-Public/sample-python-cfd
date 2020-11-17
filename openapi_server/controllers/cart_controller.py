import connexion
import six

from openapi_server.models.cart import Cart  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server import util

from openapi_server.controllers import menu_controller

# TEMPORARY IN MEMORY "DATABASE"
CART = {} # key is menu item id, value is count in cart


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
    if CART.get(int(menu_item.id)):
        CART[int(menu_item.id)]+=1
    else:
        CART.update({int(menu_item.id): 1})


def delete_cart_item(item_id):  # noqa: E501
    """Remove item from cart

    The item must be in the cart. If multiple of same item, call this twice  # noqa: E501

    :param item_id: The menu item to delete from cart
    :type item_id: int

    :rtype: None
    """
    if int(item_id) not in CART or CART.get(int(item_id)) == 0:
        return Error(403)  # cart is already devoid of this item
    CART[int(item_id)]-=1


def list_cart(limit=None):  # noqa: E501
    """List all cart items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: Cart
    """
    items = []
    for key in CART:
        items.append(menu_controller.MENU.get(key))
    # this needs to be fixed - the cart should tell you how many of the itams there should be
    return Cart(items)

