import pytest
import os
from dotenv import load_dotenv
from mongoengine.connection import _get_db

# This needs to go above the create_app import
load_dotenv(".flaskenv")

from application import create_app

@pytest.fixture
async def create_db():
    print("Creating db")
    db_test_name = os.environ["MONGODB_DB"] + "_test"
    db_host = os.environ["MONGODB_HOST"]

    # drop database if exists from previous run
    try:
        conn.execute("COMMIT")
        conn.execute(f"DROP DATABASE {db_test_name} WITH (FORCE)")
    except:
        pass

    conn.execute("COMMIT")
    conn.execute("CREATE DATABASE " + db_test_name)
    conn.close()

    print("Creating test tables")
    engine = create_engine(db_uri + db_test_name)
    metadata.bind = engine
    metadata.create_all()

    # TESTING flag disables error catching during request handling,
    # so that you get better error reports when performing test requests
    # against the application.
    yield {
        "DB_USERNAME": db_username,
        "DB_PASSWORD": db_password,
        "DB_HOST": db_host,
        "DATABASE_NAME": db_test_name,
        "DB_URI": db_uri + db_test_name,
        "TESTING": True,
    }

    print("Destroying db")
    engine = create_engine(db_uri + db_name)
    conn = engine.connect()

    conn.execute("COMMIT")
    conn.execute(f"DROP DATABASE {db_test_name} WITH (FORCE)")
    conn.close()


@pytest.fixture
async def create_test_app(create_db):
    app = create_app(**create_db)
    await app.startup()
    yield app
    await app.shutdown()


@pytest.fixture
def create_test_client(create_test_app):
    print("Creating test client")
    return create_test_app.test_client()