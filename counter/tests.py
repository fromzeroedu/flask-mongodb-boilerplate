from application import create_app as create_app_base
from mongoengine.connection import _get_db
import unittest

from counter.models import Counter
from settings import MONGODB_HOST

class CounterTest(unittest.TestCase):
    def create_app(self):
        self.db_name = 'counter_test'
        return create_app_base(
            MONGODB_SETTINGS={
                'DB': self.db_name,
                'HOST': MONGODB_HOST
                },
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY = 'mySecret!',
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def test_counter(self):
        rv = self.app.get('/')
        assert '1' in str(rv.data)
        rv = self.app.get('/')
        assert '2' in str(rv.data)
