# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMenuController(BaseTestCase):
    """MenuController integration test stubs"""

    def test_add_menu_item(self):
        """Test case for add_menu_item

        Create a menu item
        """
        menu_item = {
            "price": 6.02,
            "imageId": 5,
            "name": "name",
            "description": "description",
            "id": 13,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/menu",
            method="POST",
            headers=headers,
            data=json.dumps(menu_item),
            content_type="application/json",
        )
        self.assertStatus(
            response, 204, "Response body is : " + response.data.decode("utf-8")
        )

    def test_list_menu(self):
        """Test case for list_menu

        List all menu items
        """
        query_string = [("limit", 56)]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/menu",
            method="GET",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_show_menu_item_by_id(self):
        """Test case for show_menu_item_by_id

        Info for a specific menu item
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/menu/{item_id}".format(item_id=0), method="GET", headers=headers
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
