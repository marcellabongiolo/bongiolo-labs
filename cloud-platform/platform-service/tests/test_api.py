import pytest

from fastapi.testclient import TestClient

from app import main


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DB_PATH", tmp_path / "tasks.db")
    with TestClient(main.app) as test_client:
        yield test_client


def test_health(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert response.headers["X-Request-ID"]


def test_info(client) -> None:
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.json()["service"] == "bongiolo-platform-service"


def test_metrics(client) -> None:
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "platform_http_requests_total" in response.text


def test_create_and_list_task(client) -> None:
    created = client.post("/api/tasks", json={"title": "Deploy service"})
    assert created.status_code == 201
    assert created.json()["title"] == "Deploy service"

    listed = client.get("/api/tasks")
    assert listed.status_code == 200
    assert any(task["title"] == "Deploy service" for task in listed.json())


def test_reject_blank_task(client) -> None:
    response = client.post("/api/tasks", json={"title": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "title is required"


def test_each_test_starts_with_an_empty_database(client) -> None:
    assert client.get("/api/tasks").json() == []
