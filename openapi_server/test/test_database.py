from __future__ import absolute_import
import os
import unittest

import pytest
from flask import json
import warnings
from six import BytesIO
from sqlalchemy import exc
from openapi_server import test

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.menu_item import MenuItem  # noqa: E501
from openapi_server.test import BaseTestCase
from openapi_server.database import models, db_seed
from sqlalchemy.exc import SQLAlchemyError

# can use this to forcibly skip the db tests
SKIP_DB_TESTS = os.getenv("SKIP_DB_TESTS", True)

class TestDatabase(BaseTestCase):
    """MenuController integration test stubs"""

    def setUp(self):
        # these will only run if the postgres database is attached
        no_postgres = "postgres" not in self.app.config.get("SQLALCHEMY_DATABASE_URI")
        # converse logic is annoying, essentially we want to run the tests if the db is present, or if we say dont skip explicitly
        if no_postgres and SKIP_DB_TESTS:
                pytest.skip()
        self.open_model = models.MenuItem(
            description="description", price=6.02, image_id=5, name="name"
        )
        self.im_data = b"some file data"
        self.im_stream = BytesIO(self.im_data)
        self.im_model = models.Image(self.im_data)
        super().setUp()

    def test_add_menu_item_success(self):
        """Test case for add_menu_item
        Create a menu item
        """
        m = models.MenuItem.add(self.open_model)
        assert m.id == 1
        assert m.name == "name"
        assert m.price == 6.02
        assert m.description == "description"

    def test_add_menu_item_failure(self):
        self.open_model.price = "string"
        with pytest.raises(SQLAlchemyError):
            models.MenuItem.add(self.open_model)

    def test_menu_query(self):
        assert len([_.serialize() for _ in models.MenuItem.query_all() if _]) == 0
        db_seed.seed()
        assert len([_.serialize() for _ in models.MenuItem.query_all() if _]) >= len(
            db_seed.menu_start_raw
        )

    def test_menu_query_by_id(self):
        assert models.MenuItem.query_by_id(1) is None
        db_seed.seed()
        assert models.MenuItem.query_by_id(1) is not None

    def test_add_cart_success(self):
        db_seed.seed()
        models.Cart.add_item("1.1.1.1", models.MenuItem.query_by_id(1))

    def test_add_cart_failure(self):
        with pytest.raises(AttributeError):  # terrible, should raise a better error
            models.Cart.add_item("1.1.1.1", models.MenuItem.query_by_id(100))

    def test_list_cart(self):
        assert (
            models.Cart.query_by_host("1.1.1.1") is None
        )  # this doesn't match the menu query... this is why we do TDD!
        db_seed.seed()
        test_item = models.MenuItem.query_by_id(1)
        assert test_item.cart_id is None
        models.Cart.add_item("1.1.1.1", test_item)
        assert len(models.Cart.query_by_host("1.1.1.1").items) == 1
        assert test_item.cart_id == "1.1.1.1"

    def test_image_add_failure(self):
        with pytest.raises(SQLAlchemyError):
            models.Image.add({"bad"})

    def test_get_image(self):
        assert models.Image.get_image(0) is None
        db_seed.seed()
        m = models.Image.get_image(1)
        assert all([m.id, m.data])


if __name__ == "__main__":
    unittest.main()
