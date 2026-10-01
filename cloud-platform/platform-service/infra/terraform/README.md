# Terraform Infrastructure

This directory defines the local container infrastructure for the Platform Service.

## What it manages

- Docker image built from the application Dockerfile
- Docker container running the service
- Persistent Docker volume for SQLite data
- Configurable external port
- Terraform outputs for the service URL and resource names

## Prerequisites

- Terraform >= 1.6
- Docker

## Usage

From this directory:

```bash
terraform init
terraform plan -var-file=terraform.tfvars
terraform apply -var-file=terraform.tfvars
```

For a first run, copy the example variables:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Then verify the outputs:

```bash
terraform output
```

The default service URL is:

```
http://localhost:8000
```

## Important

Terraform state files are intentionally excluded from Git. Do not commit `terraform.tfstate`, `.tfstate.*`, or private `.tfvars` files.

## Next step

The local Docker provider is the foundation for a later cloud deployment. A cloud-specific Terraform module can be added once a target provider and deployment model are selected.
