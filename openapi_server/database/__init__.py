"""
In memory "database" using dictionaries - this could be mapped to or extended to other real dbs.

"""

import os
from openapi_server.models import MenuItem

# Technically python should load a cached module and should only run once.
# In the off change we need to make this a singleton pattern we can just use a dictionary

_has_loaded = {}
# DUMB IMAGE "DATABASE"
# key is imageId and value is path
IMAGES = {}
IMAGES_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
def _prepopulate_images():
    for f in os.listdir(IMAGES_PATH):
        if f.endswith('.jpg'):
            item_id=int(f.split('-')[0])
            ipath = os.path.join(IMAGES_PATH, f)
            IMAGES[item_id] = ipath


_prepopulate_images()

# DUMB CART "DATABASE"
CART = []

# DUMB MENU "DATABASE"
MENU = {}

menu_start_raw = [
  {
    "description": "Sample water bottle",
    "id": 0,
    "imageId": 5,
    "name": "Water",
    "price": 1.99
  },
  {
    "description": "Chicken Wrap - Sandwich",
    "id": 1,
    "imageId": 0,
    "name": "Chicken Wrap",
    "price": 14.99
  },
  {
    "description": "A slow cooked stew",
    "id": 2,
    "imageId": 4,
    "name": "Stew",
    "price": 12.99
  },
  {
    "description": "It looks good in the menu picture",
    "id": 3,
    "imageId": 3,
    "name": "Tomato Soup",
    "price": 4.99
  },
  {
    "description": "A green salad",
    "id": 4,
    "imageId": 2,
    "name": "Salad",
    "price": 4.99
  },
  {
    "description": "A single slice of pizza",
    "id": 5,
    "imageId": 1,
    "name": "Slice of pizza",
    "price": 2.99
  }
]

def _prepopulate_menu():
    for item in menu_start_raw:
        menu_item = MenuItem.from_dict(item)  # noqa: E501
        MENU[item.get('id')] = menu_item

_prepopulate_menu()