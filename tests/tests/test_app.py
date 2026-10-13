import pytest

from app import app, members


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    members.clear()
    with app.test_client() as test_client:
        yield test_client
    members.clear()


def test_home_returns_welcome_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to ACEest Fitness & Gym"


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_list_members_starts_empty(client):
    response = client.get("/members")
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_member(client):
    response = client.post("/members", json={"name": "Asha", "plan": "premium"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Asha"
    assert response.get_json()["plan"] == "premium"


def test_add_member_requires_name(client):
    response = client.post("/members", json={"plan": "standard"})
    assert response.status_code == 400
    assert "error" in response.get_json()
