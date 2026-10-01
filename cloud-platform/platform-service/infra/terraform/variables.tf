variable "service_name" {
  description = "Name used for the Docker image, container and volume."
  type        = string
  default     = "bongiolo-platform-service"
}

variable "external_port" {
  description = "Host port exposed for the platform service."
  type        = number
  default     = 8000
}
