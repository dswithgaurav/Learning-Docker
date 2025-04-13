## 🔗 Docker Networking Guide

Docker networking enables containers to communicate with each other and with the host machine. In this guide, we'll explore both **container-to-local** and **container-to-container** communication, and demonstrate how to structure a full-stack app using Docker networks.

---

### 🖥️ Container to Localhost Communication

To allow a container to talk to services running on your **local machine**, Docker provides a special DNS name:

- On **Linux/Mac**, containers can use `host.docker.internal` to reach the host machine.

Example:  
If your MongoDB is running locally on port `27017`, a container can connect to it using:  
```
mongodb://host.docker.internal:27017
```

---

### 🔄 Container to Container Communication

Containers can also communicate **with each other**, which is essential for microservices, full-stack apps, and data pipelines.

#### ✅ Requirements:
- Both containers **must be part of the same Docker network**.
- If not, you would need to hardcode the IP of the other container (not recommended due to dynamic IPs).

Once on the same network, containers can reference each other by **container name**.

---

### 📦 Full-Stack Demo with Networking

We'll demonstrate Docker networking with a **3-tier app**:
- 🛢️ **Database**: MongoDB  
- 🔧 **Backend**: Node.js REST API  
- 🌐 **Frontend**: React Single Page Application  

These services will run in separate containers and communicate via a Docker network.

<image src="images/image.png" alt="Architecture Overview" />

---

### 🚀 Run Without Docker Network (Using localhost)

This setup makes services available on host ports, but doesn't allow inter-container communication:
```bash
# Start MongoDB
docker run --name mongodb --rm -d -p 27017:27017 mongo

# Build and run Node.js backend
docker build -t goals-node .
docker run --name goals-backend --rm -d -p 80:80 goals-node

# Build and run React frontend
docker build -t goals-react .
docker run --name goals-frontend --rm -d -p 3000:3000 -it goals-react
```

In this setup, the backend must use `host.docker.internal` to talk to MongoDB, which is not ideal for container orchestration or production.

---

### 🌐 Run With Docker Network (Preferred)

We'll now create a user-defined bridge network so containers can reference each other by name:

```bash
# Create a custom network
docker network create goals-net
```

#### 🛢️ MongoDB (with volume for persistence)
```bash
docker run --name mongodb \
  --rm -d \
  --network goals-net \
  -v named_volume:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=gaurav \
  -e MONGO_INITDB_ROOT_PASSWORD=secret \
  mongo
```

#### 🔧 Backend (Node.js)
```bash
docker build -t goals-node .
docker run --name goals-backend \
  --rm -d \
  --network goals-net \
  -p 80:80 \
  goals-node
```

> The backend will now access MongoDB using the hostname `mongodb` (the container name).

#### 🌐 Frontend (React)
```bash
docker build -t goals-react .
docker run --name goals-frontend \
  --rm -d \
  -p 3000:3000 \
  -it goals-react
```

> Since the frontend runs in the browser on the host machine, it doesn't need to be in the Docker network.

---

### ✅ Summary

| Component | Role | Docker Network | Host Port | Notes |
|----------|------|----------------|-----------|-------|
| MongoDB  | Database | Yes (goals-net) | 27017 (optional) | Accessed by backend as `mongodb` |
| Node.js  | Backend API | Yes (goals-net) | 80 | Talks to MongoDB |
| React    | Frontend SPA | No | 3000 | Runs in browser, accesses backend via `localhost:80` |

---

We will discuss Docker Compose to simplify this setup further!