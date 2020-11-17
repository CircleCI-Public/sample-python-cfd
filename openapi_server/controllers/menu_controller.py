import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server import util

# TEMPORARY IN MEMORY "DATABASE"
MENU = {0: MenuItem(id=0,description="Sample",name="Sample",price=.50,image_url="https://en.wikipedia.org/wiki/Costco#/media/File:Kirkland_Signature_Drinking_Water_1.5L_20050508.jpg"),
}

def add_menu_item():  # noqa: E501
    """Create a menu item

    Creates a new item in the menu. Duplicates are allowed # noqa: E501

    :param menu_item: Item to add to the store
    :type menu_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        menu_item = MenuItem.from_dict(connexion.request.get_json())  # noqa: E501
    if MENU.get(int(menu_item.id)):
        return Error(400)
    else:
        MENU.update({int(menu_item.id): menu_item})


def list_menu(limit=None):  # noqa: E501
    """List all menu items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[MenuItem]
    """
    values = list(MENU.values())[:limit] if limit else list(MENU.values())[:100]
    return values

def show_menu_item_by_id(item_id):  # noqa: E501
    """Info for a specific menu item

     # noqa: E501

    :param item_id: The id of the menu item to retrieve
    :type item_id: str

    :rtype: MenuItem
    """
    return MENU.get(int(item_id))
