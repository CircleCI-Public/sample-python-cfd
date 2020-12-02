# coding: utf-8

from __future__ import absolute_import
import unittest
from unittest import mock

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.test import BaseTestCase

from openapi_server.controllers import image_controller


class TestImageController(BaseTestCase):
    """ImageController integration test stubs"""

    # @unittest.skip('reason')
    def test_add_image(self):
        """Test case for add_image

        Add an image to the restaraunt
        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "multipart/form-data",
        }
        data = dict(fileName=(BytesIO(b"some file data"), "file.png"))
        response = self.client.open(
            "/CFD/1.0.0/image",
            method="POST",
            headers=headers,
            data=data,
            content_type="multipart/form-data",
        )
        try:
            e = None
            self.assert200(
                response, "Response body is : " + response.data.decode("utf-8")
            )
        except BaseException as e:
            raise
        finally:
            image_controller.delete_image(response.get_json().get("imageId"))

    @mock.patch("os.remove")
    def test_delete_image(self, mock_remove):
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
        assert mock_remove.call_count == 1

    def test_get_image(self):
        """Test case for get_image

        Get image
        """
        self.test_add_image()
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
