from starlette.testclient import TestClient

from sql_app.main import app

client = TestClient(app)


def test_locations_postgres():
    response = client.get("/get_using_postgres/28.6333&77.2167&5")
    assert response.status_code == 200


def test_locations_postgres_existing():
    response = client.get("/get_using_postgres/28&77&5")
    assert response.status_code == 404
    assert response.json() == {"detail": "Latitude and Longitude are not exist."}


def test_locations_self():
    response = client.get("/get_using_self/28.6333&77.2167&5")
    assert response.status_code == 200


def test_locations_self_existing():
    response = client.get("/get_using_self/28&77&5")
    assert response.status_code == 404
    assert response.json() == {"detail": "Latitude and Longitude are not exist."}


def test_compare():
    response_postgres = client.get("/get_using_postgres/28.6333&77.2167&5") 
    response_self = client.get("/get_using_self/28.6333&77.2167&5")
    assert response_postgres.json() != response_self.json()