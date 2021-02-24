"""
In memory "database" using dictionaries - this could be mapped to or extended to other real dbs.

"""

import os
from openapi_server.models import MenuItem
from openapi_server.database import models

# Technically python should load a cached module and should only run once.
# In the off change we need to make this a singleton pattern we can just use a dictionary

IMAGES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

menu_start_raw = [
    {
        "description": "Sample water bottle",
        "id": 0,
        "imageId": "water",
        "name": "Water",
        "price": 1.99,
    },
    {
        "description": "Chicken Wrap - Sandwich",
        "id": 1,
        "imageId": "wrap",
        "name": "Chicken Wrap",
        "price": 14.99,
    },
    {
        "description": "A slow cooked stew",
        "id": 2,
        "imageId": "stew",
        "name": "Stew",
        "price": 12.99,
    },
    {
        "description": "It looks good in the menu picture",
        "id": 3,
        "imageId": "soup",
        "name": "Tomato Soup",
        "price": 4.99,
    },
    {
        "description": "A green salad",
        "id": 4,
        "imageId": "salad",
        "name": "Salad",
        "price": 4.99,
    },
    {
        "description": "A single slice of pizza",
        "id": 5,
        "imageId": "pizza",
        "name": "Slice of pizza",
        "price": 2.99,
    },
]

def _prepopulate_images():
    for f in os.listdir(IMAGES_PATH):
        if f.endswith(".jpg"):
            name = f.split(".")[0]
            ipath = os.path.join(IMAGES_PATH, f)
            with open(ipath, 'rb') as f2:
                raw = f2.read()
            image = models.Image.add(raw)
            # super inefficient
            for mi in menu_start_raw:
                if mi.get('imageId') == name :
                    mi.update({'imageId': image.id})


def _prepopulate_menu():
    for item in menu_start_raw:
        print(item)
        menu_item = MenuItem.from_dict(item)  # noqa: E501
        models.MenuItem.add(menu_item)


def seed():
    _prepopulate_images()
    _prepopulate_menu()
