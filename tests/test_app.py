
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_welcome_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_members_returns_empty_list(client):
    response = client.get("/members")
    assert response.status_code == 200
    assert response.json == []


def test_add_member_success(client):
    response = client.post("/members", json={"name": "Ravi"})
    assert response.status_code == 201
    assert response.json["name"] == "Ravi"


def test_add_member_requires_name(client):
    response = client.post("/members", json={})
    assert response.status_code == 400


def test_get_existing_member(client):
    response = client.post("/members", json={"name": "Priya"})
    member_id = response.json["id"]

    response = client.get(f"/members/{member_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Priya"


def test_missing_member_returns_404(client):
    response = client.get("/members/999")
    assert response.status_code == 404
