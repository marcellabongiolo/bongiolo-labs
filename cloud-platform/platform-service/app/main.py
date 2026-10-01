from pathlib import Path
import sqlite3

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.observability import request_observability


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path("/app/data/platform.db")
WEB_PATH = BASE_DIR / "web" / "index.html"

app = FastAPI(title="Bongiolo Platform Service", version="1.0.0")
app.middleware("http")(request_observability)


class Task(BaseModel):
    title: str


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS tasks "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)"
        )


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/")
def home() -> FileResponse:
    return FileResponse(WEB_PATH)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/info")
def info() -> dict[str, str]:
    return {"service": "bongiolo-platform-service", "version": "1.0.0"}


@app.get("/api/tasks")
def list_tasks() -> list[dict[str, object]]:
    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute(
            "SELECT id, title FROM tasks ORDER BY id DESC"
        ).fetchall()

    return [{"id": row[0], "title": row[1]} for row in rows]


@app.post("/api/tasks", status_code=201)
def create_task(task: Task) -> dict[str, object]:
    title = task.title.strip()
    if not title:
        return {"error": "title is required"}

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title) VALUES (?)", (title,)
        )
        task_id = cursor.lastrowid

    return {"id": task_id, "title": title}
