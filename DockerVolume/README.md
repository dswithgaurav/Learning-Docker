
## 📘 Table of Contents
- Images, Containers & Volumes  
- Arguments & Environment Variables  
- Data Persistence Strategies  
- Docker Build & Run Steps  
- Volumes & Bind Mounts  


## 📦 Data Types in Containers

Understanding where and how data is stored is key to building reliable Dockerized applications.

### 1. **Application Code & Dependencies**
- Added during the `docker build` phase via `Dockerfile`
- Immutable after build
- 🔒 **Stored in Image**
> _E.g., FastAPI app code, Python libraries, system packages_

---

### 2. **Temporary Runtime Data**
- Exists only during the container's lifecycle
- Lost when the container stops
- 🧠 **Stored in Container Layer**
> _E.g., in-memory data, temp files, user session data_

---

### 3. **Persistent Data**
- Must survive container restarts or rebuilds
- 💾 **Stored in Volumes or Bind Mounts**
> _E.g., uploaded files, logs, databases (SQLite), user content_

---

## 🚀 Docker Commands

### 🔨 Build the Image
```bash
docker build -t fastapi-app .
```

### ▶️ Run the Container with Volume
```bash
docker run --name my_container --rm -p 1000:8000 -v logme:/app/logs fastapi-app
```

---

## 🗂️ Understanding Volumes

Volumes are **managed by Docker** and stored on the host file system. They're used to persist data **outside the container**.

- Automatically created if not existing
- Data is preserved even if the container is deleted
- Preferred over bind mounts for production

📌 Example Volume Mapping:
```
Host Path         →    Container Path
logme:/app/logs   →    Container logs directory
```

---

## 🧰 Volume Types

### 1. **Anonymous Volumes**
- Created without a name
- Used temporarily
- Removed when the container is deleted (unless retained manually)

```bash
docker run -v /app/temp-data fastapi-app
```

### 2. **Named Volumes**
- Explicitly named and reusable
- Good for persistent storage
- Can be inspected via `docker volume ls`

```bash
docker run -v logs:/app/logs fastapi-app
```

You can also inspect volume content using a temporary container:
```bash
docker run -it --rm -v logs:/app busybox sh
```

---

## 🔄 Bind Mounts

Bind mounts map a **specific folder on the host** to a path inside the container.

- Offers full control of the host path  
- Useful for local development (live code changes)

```bash
docker run -v $(pwd)/data:/app/data fastapi-app
```

📌 **Difference vs. Volumes**:
| Feature         | Volumes         | Bind Mounts       |
|-----------------|-----------------|-------------------|
| Managed by      | Docker          | You (host system) |
| Portability     | ✅ Yes           | ❌ No              |
| Dev Friendly    | ❌ Less ideal    | ✅ Great for local dev |
| Performance     | ✅ Better        | ⚠️ Depends on OS   |

---
