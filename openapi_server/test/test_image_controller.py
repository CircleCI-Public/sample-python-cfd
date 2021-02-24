# coding: utf-8

from __future__ import absolute_import
import unittest
from unittest import mock

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.test import BaseTestCase
from openapi_server.database import models


from openapi_server.controllers import image_controller


class TestImageController(BaseTestCase):
    """ImageController integration test stubs"""

    def setUp(self):
        self.mock_data = b"some file data"
        self.mock_stream = BytesIO(self.mock_data)
        self.mock_model = models.Image(self.mock_data)

    # @unittest.skip('reason')
    @mock.patch.object(models.Image, "add")
    def test_add_image(self, mock_add):
        """Test case for add_image

        Add an image to the restaraunt
        """
        mock_add.return_value = self.mock_model
        headers = {
            "Accept": "application/json",
            "Content-Type": "multipart/form-data",
        }
        data = dict(fileName=(self.mock_stream, "file.png"))
        response = self.client.open(
            "/CFD/1.0.0/image",
            method="POST",
            headers=headers,
            data=data,
            content_type="multipart/form-data",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    @mock.patch.object(models.Image, "delete_image")
    def test_delete_image(self, mock_delete):
        """Test case for delete_image

        Remove image
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/image/{image_id}".format(image_id=0),
            method="DELETE",
            headers=headers,
        )
        self.assertStatus(
            response, 204, "Response body is : " + response.data.decode("utf-8")
        )
        assert mock_delete.call_count == 1

    @mock.patch.object(models.Image, "get_image")
    def test_get_image(self, mock_get):
        """Test case for get_image

        Get image
        """
        mock_get.return_value = self.mock_model
        headers = {
            "Accept": "image/png application/json",
        }
        response = self.client.open(
            "/CFD/1.0.0/image/{image_id}".format(image_id=0),
            method="GET",
            headers=headers,
        )
        self.assert200(response)


if __name__ == "__main__":
    unittest.main()
