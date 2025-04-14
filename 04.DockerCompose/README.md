
# Docker Compose Guide

## 🚀 What is Docker Compose?

Docker Compose is a tool used to define and run multi-container Docker applications. It allows you to automate the setup and management of containers using a single `docker-compose.yml` file.

### ✅ Benefits
- **Automates multi-container setup**: Define services, networks, and volumes in a single file.
- **Replaces manual Docker commands**: No need to run multiple `docker run` commands.
- **Makes local development faster and more consistent.**

---

## 🚫 What Docker Compose is NOT for

- ❌ **Not a replacement for Dockerfiles**: You still need Dockerfiles to build custom images.
- ❌ **Does not replace Docker images or containers**: It uses existing images and configurations.
- ❌ **Not ideal for multi-host setups**: For orchestrating containers across multiple machines, use tools like Kubernetes or Docker Swarm.

---

## ✍️ Writing a Compose File

Here’s how you can start writing your `docker-compose.yml` file:

- Define services (containers) with their build paths or images.
- Configure ports, environment variables, and volumes.
- Use `depends_on` to define service dependencies.
- Use named volumes for persistent storage and shared logs.

---

## 📂 Sample Docker Compose File

This file is based on the `03.CrossContainerCommunication` module:

```yaml
version: "3.8"

services:
  mongodb:
    image: "mongo"
    volumes:
      - data:/data/db
    environment:
      - MONGO_INITDB_ROOT_USERNAME=gaurav
      - MONGO_INITDB_ROOT_PASSWORD=secret 

  backend:
    build: ./src/backend/
    ports:
      - '80:80'
    environment:
      - MONGODB_USERNAME=gaurav
      - MONGODB_PASSWORD=secret
    volumes:
      - logs:/app/logs
      - /Users/gaurav/backend:/app
      - /app/node_modules
    depends_on:
      - mongodb  

  frontend:
    build: ./src/frontend/
    ports:
      - '3000:3000'
    volumes:
      - /Users/gaurav/development/src:/app/src
    stdin_open: true
    tty: true
    
volumes:
  data:
  logs:
```

---

## 📦 Common Commands

```bash
# Start the application in the background
docker-compose up -d

# Stop and remove containers, networks, and volumes defined in the file
docker-compose down

# Rebuild services
docker-compose up --build

# View logs from all services
docker-compose logs

# Run a one-off command in a service container
docker-compose run <service_name> <command>
```

---

## 📌 Tips

- Use `.env` files to avoid hardcoding environment variables.
- Use volume mounts for live code reloads during development.
- Prefer named volumes for persistent data instead of anonymous ones.