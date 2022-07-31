import pytest
from sojern_app import application


@pytest.fixture
def app():
    test_app = application.sojern_math_app
    test_app.config.update({
        "TESTING": True,
    })

    yield test_app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_min(client):
    response = client.get("/min?numbers=10,5,4,7,8,18&k=3")
    assert b"4, 5, 7" in response.data

def test_request_min_no_k(client):
    response = client.get("/min?numbers=10,5,4,7,8,18")
    assert b"4" in response.data

def test_request_max(client):
    response = client.get("/max?numbers=10,5,4,7,8,18&k=3")
    assert b"18, 10, 8" in response.data

def test_request_max_no_k(client):
    response = client.get("/max?numbers=10,5,4,7,8,18")
    assert b"18" in response.data

def test_request_avg(client):
    response = client.get("/avg?numbers=10,5,4,7,8,18")
    assert b"8.667" in response.data

def test_request_median(client):
    response = client.get("/median?numbers=10,5,4,7,8,18")
    assert b"7.5" in response.data

def test_request_percentile(client):
    response = client.get("/percentile?numbers=10,5,4,7,8,18&q=25")
    assert b"5" in response.data
