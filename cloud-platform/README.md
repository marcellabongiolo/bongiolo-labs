# Cloud & Platform

This area contains infrastructure and platform-engineering experiments.

## Platform Service Lab

The first implemented service is an end-to-end FastAPI application with a browser interface, SQLite persistence, Docker packaging and automated GitHub Actions validation.

Project: `cloud-platform/platform-service/`

Architecture:

```
Browser
   ↓
FastAPI
   ↓
SQLite
   ↑
Docker volume

GitHub Push / PR
   ↓
GitHub Actions
   ├── Install
   ├── Test
   └── Build image
```

## Implemented capabilities

- API health checks
- REST task endpoints
- Browser interface
- Persistent data volume
- Automated tests
- Docker image
- Docker Compose
- CI pipeline

## Next platform capabilities

- Observability and structured logging
- Infrastructure as Code
- Cloud deployment
- Service metrics
- Reliability documentation
- Security hardening

The platform layer will evolve as the lab's products require more infrastructure.
