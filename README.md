## Learniing Docker

Here’s a list of essential **Docker commands** in Bash, categorized for easy reference.  

### 🔹 **Basic Docker Commands**  
```bash
docker --version                     # Check Docker version  
docker info                           # Display system-wide information  
docker help                           # Show help for Docker commands  
```

### 🔹 **Container Management**  
```bash
docker ps                             # List running containers  
docker ps -a                          # List all containers (including stopped ones)  
docker run -d --name my_container image_name  # Run a container in detached mode  
docker start container_id/name        # Start a stopped container  
docker stop container_id/name         # Stop a running container  
docker restart container_id/name      # Restart a container  
docker rm container_id/name           # Remove a container  
docker logs container_id/name         # View container logs  
docker inspect container_id/name      # Get detailed information about a container  
docker exec -it container_id/name bash  # Access a running container's shell  
docker attach container_id/name       # Attach to a running container  
docker kill container_id/name         # Forcefully stop a container  
```

### 🔹 **Image Management**  
```bash
docker images                         # List available images  
docker pull image_name                 # Download an image from Docker Hub  
docker push image_name                  # Upload an image to Docker Hub  
docker rmi image_id/name               # Remove an image  
docker tag source_image target_image   # Tag an image  
docker inspect image_id/name           # Get image details  
```

### 🔹 **Docker Volumes & Networks**  
```bash
docker volume ls                      # List volumes  
docker volume create volume_name      # Create a volume  
docker volume rm volume_name          # Remove a volume  
docker network ls                      # List networks  
docker network create network_name    # Create a network  
docker network rm network_name        # Remove a network  
```

### 🔹 **Build & Manage Dockerfiles**  
```bash
docker build -t image_name .           # Build an image from a Dockerfile  
docker history image_name               # Show history of an image  
```

### 🔹 **Docker Compose**  
```bash
docker-compose up -d                   # Start services in the background  
docker-compose down                    # Stop and remove containers/networks  
docker-compose logs                     # View logs for all services  
docker-compose ps                      # List services and their states  
```

### 🔹 **Monitor & Debug Containers**  
```bash
docker stats                           # Display resource usage (CPU, Memory, etc.)  
docker top container_id/name           # Show running processes inside a container  
docker events                          # Show real-time Docker events  
docker diff container_id/name          # Show changes in the container filesystem  
```

### 🔹 **Clean Up Unused Docker Resources**  
```bash
docker system prune -a                 # Remove all stopped containers, images, and networks  
docker container prune                  # Remove all stopped containers  
docker volume prune                     # Remove unused volumes  
docker network prune                    # Remove unused networks  
docker image prune                      # Remove unused images  
```

### 🔹 **Copying from/to Container**  
```bash
docker cp local.txt container_id:/test/ # Copy from local to container
docker cp container_id:/test/ local.txt # Copy from container to local
```
