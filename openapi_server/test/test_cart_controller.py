# coding: utf-8

from __future__ import absolute_import
import unittest
from unittest import mock

from flask import json
from six import BytesIO

from openapi_server.models.cart import Cart  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server.test import BaseTestCase
from openapi_server.database import models


class TestCartController(BaseTestCase):
    """CartController integration test stubs"""

    def setUp(self):
        self.sample_model = models.MenuItem(
            description="description", price=6.02, image_id=5, name="name"
        )
        self.sample_cart = models.Cart("fake")
        self.sample_cart.items = [self.sample_model]
        self.sample_item = {
            "price": 6.02,
            "imageId": 5,
            "name": "name",
            "description": "description",
            "id": 13,
        }

    @mock.patch.object(models.Cart, "add_item")
    def test_add_cart_item(self, mock_add_item):
        """Test case for add_cart_item

        Add a menu item a cart
        """
        menu_item = {
            "price": 6.027456183070403,
            "imageId": 5,
            "name": "name",
            "description": "description",
            "id": 0,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/cart",
            method="POST",
            headers=headers,
            data=json.dumps(menu_item),
            content_type="application/json",
        )
        self.assertStatus(
            response, 204, "Response body is : " + response.data.decode("utf-8")
        )

    @mock.patch.object(models.Cart, "delete_item_by_id")
    def test_delete_cart_item(self, mock_delete):
        """Test case for delete_cart_item

        Remove item from cart
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/cart/{item_id}".format(item_id=56),
            method="DELETE",
            headers=headers,
        )
        self.assertStatus(
            response, 204, "Response body is : " + response.data.decode("utf-8")
        )

    @mock.patch.object(models.Cart, "query_by_host")
    def test_list_cart(self, mock_get_cart):
        """Test case for list_cart

        List all cart items
        """
        mock_get_cart.return_value = self.sample_cart
        query_string = [("limit", 56)]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/cart",
            method="GET",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
