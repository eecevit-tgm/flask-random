import json
import pytest
import unittest
import requests
from run import app as create_app
import logging

@pytest.fixture
def client():
    create_app.testing = True
    client = create_app.test_client()
    yield client


def test_check(client):
    res = requests.get('http://localhost:8080/api/random')
    assert 'randomNumber' in res.json()


def test_range(client):
    res = requests.get('http://localhost:8080/api/random')
    logging.info("Random Number: ")
    logging.info(res.json()['randomNumber'])
    assert res.json()['randomNumber'] <= 100
    assert res.json()['randomNumber'] >= 1
