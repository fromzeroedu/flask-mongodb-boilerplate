import pytest
from flask import current_app

from counter.models import Counter


def test_initial_response(create_test_client):
    response = create_test_client.get("/")
    body = response.get_data()
    assert "Counter: 1" in str(body)


def test_second_response(create_test_app, create_test_client):
    # Counter 1
    response = create_test_client.get("/")
    body = response.get_data()

    # Counter 2
    response = create_test_client.get("/")
    body = response.get_data()
    assert "Counter: 2" in str(body)

    # check on the model itself
    with create_test_app.app_context():
        counter = Counter.objects.all().first()
        assert counter.count == 2
