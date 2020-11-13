import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server import util


def add_menu_item(menu_item):  # noqa: E501
    """Create a menu item

    Creates a new item in the menu. Duplicates are allowed # noqa: E501

    :param menu_item: Item to add to the store
    :type menu_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        menu_item = MenuItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_menu(limit=None):  # noqa: E501
    """List all menu items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[MenuItem]
    """
    return 'do some magic!'


def show_menu_item_by_id(item_id):  # noqa: E501
    """Info for a specific menu item

     # noqa: E501

    :param item_id: The id of the menu item to retrieve
    :type item_id: str

    :rtype: MenuItem
    """
    return 'do some magic!'
