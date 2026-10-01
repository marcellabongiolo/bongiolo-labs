# Cloud Deployment Architecture

This directory documents the cloud-ready deployment boundary for the Platform Service.

## Current architecture

The application is packaged as a Docker image and currently runs locally through Docker Compose or Terraform.

## Cloud target

The service is designed to move toward a managed container platform:

```
GitHub
  |
  v
CI
  |
  v
Container image
  |
  v
Managed container service
  |
  +--> HTTPS endpoint
  |
  +--> Application logs
  |
  +--> Metrics
  |
  +--> Persistent data service
```

## Deployment principles

- Keep the application container stateless where possible.
- Do not store secrets in Git.
- Expose the service through HTTPS in production.
- Collect application logs centrally.
- Monitor request latency, errors and traffic.
- Use a managed persistent database instead of local SQLite when multiple instances or production durability are required.
- Keep infrastructure configuration versioned and reproducible.

## Production evolution

The current SQLite volume is appropriate for the local lab. A production deployment should replace it with a managed database before scaling the service horizontally.

The next implementation step is provider-specific infrastructure after selecting the target cloud platform.
