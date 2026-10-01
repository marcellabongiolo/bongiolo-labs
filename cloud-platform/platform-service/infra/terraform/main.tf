terraform {
  required_version = ">= 1.6.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "platform_service" {
  name = "${var.service_name}:latest"

  build {
    context    = "../../"
    dockerfile = "Dockerfile"
  }
}

resource "docker_volume" "platform_data" {
  name = "${var.service_name}-data"
}

resource "docker_container" "platform_service" {
  name  = var.service_name
  image = docker_image.platform_service.image_id

  ports {
    internal = 8000
    external = var.external_port
  }

  volumes {
    volume_name    = docker_volume.platform_data.name
    container_path = "/app/data"
  }

  restart = "unless-stopped"
}
