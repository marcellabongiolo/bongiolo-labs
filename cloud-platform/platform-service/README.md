# Platform Service Lab

A small end-to-end cloud/platform engineering project built by Bongiolo Labs.

## Stack

- Python + FastAPI
- SQLite
- Docker
- HTML/CSS/JavaScript frontend
- pytest
- GitHub Actions

## Architecture

```
Browser
   |
   v
FastAPI application
   |
   v
SQLite
```

## Features

- Health endpoint
- Service information endpoint
- Persistent task creation and listing
- Minimal browser interface
- Automated tests
- Request IDs and request-duration logging
- Containerized execution
- CI validation

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000`.

## Run with Docker

```bash
docker compose up --build
```

## Tests

```bash
pytest -q
```

## Engineering goals

This lab demonstrates the path from application code to a repeatable platform workflow: build, test, package, run, observe and improve.
