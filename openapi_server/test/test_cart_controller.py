# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.cart import Cart  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCartController(BaseTestCase):
    """CartController integration test stubs"""

    def test_add_cart_item(self):
        """Test case for add_cart_item

        Add a menu item a cart
        """
        menu_item = {
  "price" : 6.027456183070403,
  "imageUrl" : "imageUrl",
  "name" : "name",
  "description" : "description",
  "id" : 0
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/dsayling8/ZoomFoodToo/1.0.0/cart',
            method='POST',
            headers=headers,
            data=json.dumps(menu_item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cart_item(self):
        """Test case for delete_cart_item

        Remove item from cart
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dsayling8/ZoomFoodToo/1.0.0/cart/{item_id}'.format(item_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_cart(self):
        """Test case for list_cart

        List all cart items
        """
        query_string = [('limit', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/dsayling8/ZoomFoodToo/1.0.0/cart',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
