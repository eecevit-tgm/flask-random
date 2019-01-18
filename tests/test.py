import json
import pytest
import unittest
from run import app as create_app

@pytest.fixture
def client():
    create_app.testing = True
    client = create_app.test_client()
    yield client

def test_show_users(client):
    rv = client.get('/api/random')
    self.assertTrue(1 <= rv.data <= 100)