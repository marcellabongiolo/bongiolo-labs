output "service_name" {
  description = "Docker container name."
  value       = docker_container.platform_service.name
}

output "service_url" {
  description = "Local URL for the running platform service."
  value       = "http://localhost:${var.external_port}"
}

output "volume_name" {
  description = "Persistent Docker volume used by the service."
  value       = docker_volume.platform_data.name
}
