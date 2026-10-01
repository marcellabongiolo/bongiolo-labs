output "ecr_repository_url" {
  description = "ECR repository URL for the platform service image."
  value       = aws_ecr_repository.platform_service.repository_url
}

output "cloudwatch_log_group" {
  description = "CloudWatch log group for the platform service."
  value       = aws_cloudwatch_log_group.platform_service.name
}
