# Cloud & Platform

This area contains infrastructure and platform-engineering experiments.

## Platform Service Lab

The first implemented service is an end-to-end FastAPI application with a browser interface, SQLite persistence, Docker packaging, automated GitHub Actions validation, Prometheus-compatible service metrics and Terraform infrastructure definition.

Project: `cloud-platform/platform-service/`

Architecture:

```
Browser
   ↓
FastAPI
   ├── SQLite
   └── /metrics
        ↓
   Prometheus-compatible metrics

Request
   ↓
Observability middleware
   ├── Request ID
   ├── Request count
   ├── Error count
   └── Request latency

Terraform
   ↓
Docker image
   ↓
Platform service container
   ↓
Persistent Docker volume

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
- Local database path configuration
- Automated tests
- Docker image
- Docker Compose
- CI pipeline
- Request IDs
- Request-duration logging
- Prometheus-compatible request metrics
- HTTP 5xx error tracking
- Terraform infrastructure definition

## Next platform capabilities

- Cloud deployment
- Metrics dashboard
- Reliability documentation
- Security hardening

The platform layer will evolve as the lab's products require more infrastructure.
