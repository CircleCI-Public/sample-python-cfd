import connexion

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server.database import models
from sqlalchemy.exc import SQLAlchemyError


def add_menu_item():  # noqa: E501
    """Create a menu item

    Creates a new item in the menu. Duplicates are allowed # noqa: E501

    :param menu_item: Item to add to the store
    :type menu_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            menu_item = MenuItem.from_dict(connexion.request.get_json())  # noqa: E501
            return models.MenuItem.add(menu_item).serialize()
        except (SQLAlchemyError, TypeError):
            models.db.session.rollback()
            return Error(400), 400
    else:
        return Error(400), 400


def list_menu(limit=None):  # noqa: E501
    """List all menu items

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[MenuItem]
    """
    # todo setup limit by using paginate
    values = [_.serialize() for _ in models.MenuItem.query_all() if _]
    return values


def show_menu_item_by_id(item_id):  # noqa: E501
    """Info for a specific menu item

     # noqa: E501

    :param item_id: The id of the menu item to retrieve
    :type item_id: str

    :rtype: MenuItem
    """
    if (item := models.MenuItem.query_by_id(int(item_id))) :
        return item.serialize()
    else:
        return Error(400), 400
