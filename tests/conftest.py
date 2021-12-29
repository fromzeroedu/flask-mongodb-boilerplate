import pytest
import os
from dotenv import load_dotenv
from mongoengine.connection import _get_db

# This needs to go above the create_app import
load_dotenv(".flaskenv")

from application import create_app


@pytest.fixture
def create_db():
    print("Creating db")
    db_test_name = os.environ["MONGODB_DB"] + "_test"
    db_host = os.environ["MONGODB_HOST"]

    # there's no need to drop the database prior if unhealthy
    # since it's dropped automatically after tests are run

    # TESTING flag disables error catching during request handling,
    # so that you get better error reports when performing test requests
    # against the application.
    yield {
        "MONGODB_HOST": db_host,
        "MONGODB_DB": db_test_name,
        "TESTING": True,
    }

    print("Destroying db")
    db = _get_db()
    db.client.drop_database(db)


@pytest.fixture
def create_test_app(create_db):
    app = create_app(**create_db)
    yield app


@pytest.fixture
def create_test_client(create_test_app):
    print("Creating test client")
    return create_test_app.test_client()
