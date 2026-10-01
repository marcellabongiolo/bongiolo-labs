# AWS Deployment Target

The first provider-specific target for the Platform Service is Amazon ECS on AWS Fargate.

AWS Fargate runs containers without requiring management of the underlying EC2 server fleet. Amazon ECR can store the container image that ECS/Fargate pulls for deployment.

## Target architecture

```
GitHub Actions
     |
     v
Amazon ECR
     |
     v
Amazon ECS
     |
     v
AWS Fargate task
     |
     +--> HTTP/HTTPS endpoint
     +--> CloudWatch logs
     +--> Prometheus-compatible application metrics
```

## Application requirements

The current application already provides:

- Docker image
- HTTP health endpoint at `/health`
- Prometheus-compatible metrics at `/metrics`
- Request IDs
- Request latency tracking
- HTTP error tracking

## Important storage decision

The current application persists tasks in SQLite. A Fargate deployment should not treat the local container filesystem as durable application storage.

Before production scaling, the persistence layer should move to a managed database. The cloud deployment should therefore be treated as a deployment architecture and staging target until that migration is complete.

## Planned AWS resources

The implementation can be expanded into Terraform-managed resources for:

1. ECR repository
2. ECS cluster
3. ECS task definition
4. ECS service
5. IAM execution role
6. Networking/security groups
7. Application Load Balancer
8. CloudWatch log group

No AWS credentials or secrets belong in this repository.
