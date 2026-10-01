from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert response.headers["X-Request-ID"]


def test_info() -> None:
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.json()["service"] == "bongiolo-platform-service"


def test_metrics() -> None:
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "platform_http_requests_total" in response.text


def test_create_and_list_task() -> None:
    created = client.post("/api/tasks", json={"title": "Deploy service"})
    assert created.status_code == 201
    assert created.json()["title"] == "Deploy service"

    listed = client.get("/api/tasks")
    assert listed.status_code == 200
    assert any(task["title"] == "Deploy service" for task in listed.json())


def test_reject_blank_task() -> None:
    response = client.post("/api/tasks", json={"title": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "title is required"
